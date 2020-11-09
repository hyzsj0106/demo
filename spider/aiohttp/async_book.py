# 导入模块
import asyncio
import aiohttp
import logging
# 异步存储库
from motor.motor_asyncio import AsyncIOMotorClient

# 连接本地mongodb
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.spider_test
collection = db.books

# 配置日志信息
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

# 定义索引页、详情页接口url
INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/{}/'
# 定目标页数
Flags = 50
# 显示数量
LIMIT = 18
# 并发量
CONCURRENCY = 10
sem = asyncio.Semaphore(CONCURRENCY)
# 爬取失败的url列表
index_fail = []
detail_fail = []


# 爬取接口
async def fetch(url):
	# 信号量上下文管理器
    async with sem:
        try:
        	# 如果获取正确，返回索引页详情
            logging.info("scraping session_id %s ,url: %s", id(session), url)
            async with session.get(url) as response:
                await asyncio.sleep(1)
                return await response.json()
        except:
        	# 报错 返回响应状态码、url
            logging.error("Error code:%s, scraped url:%s", response.status, url)
            return {'Code': response.status, 'url': url}


# 获取索引页
async def scrape_index(page):
    url = INDEX_URL.format((page - 1) * LIMIT)
    return await fetch(url)


# 获取详情页
async def scrape_detail(isbn):
    url = DETAIL_URL.format(isbn)
    data = await fetch(url)
    await save_data(data)

# 保存内容
async def save_data(data):
    logging.info('data: %s', data)
    if 'Code' not in data:
        try:
        	# 尝试保存，失败记录下来
            await collection.update_one({
                    'id': data.get('id')
                }, {'$set': data
                }, upsert=True
            )
        except:
            logging.info("save data failed")
    else:
    	# 将错误状态码的url保存到列表
        detail_fail.append(data.get('url'))


async def main():
    global session
    # 创建一个session对象，上下文管理器，无需关闭
    async with aiohttp.ClientSession() as session:
    	# 创建一个含协程对象的列表
        index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, Flags + 1)]
        # 将tasks注册到时间循环上，并接收结果
        index_results = await asyncio.gather(*index_tasks)
        for results in index_results:
            if 'Code' in results:
            	# 将报错的url保存起来
                index_fail.append(results.get('url'))
                continue
            # 创建一个包含所有id的列表
            isbns = [_.get('id') for _ in results.get('results')]
            # 获取详情页的tasks列表
            isbn_tasks = [asyncio.ensure_future(scrape_detail(isbn)) for isbn in isbns]
            # 无需返回值，所以可以用wait方法
            await asyncio.wait(isbn_tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    logging.info('index_fail len: %s , list: %s ', len(index_fail), index_fail)
    logging.info('detail_fail len: %s , list: %s ', len(detail_fail), detail_fail)
