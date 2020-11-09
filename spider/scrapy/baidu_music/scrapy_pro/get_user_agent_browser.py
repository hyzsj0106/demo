# -*- coding: utf-8 -*-

# 导入包
import requests
import random
import json

# 获取user-agent并保存为json文件
def get_user_agent_browsers():
    # 确定目标url
    user_agent_url = 'http://fake-useragent.herokuapp.com/browsers/0.1.11'
    # 获取内容
    response = requests.get(user_agent_url)
    # 保存内容
    with open('browsers.json', 'w') as f:
        json.dump(response.text, f)
        f.write('\n')

# 获取本地json文件中的browsers
def get_random_browsers():

    with open('browsers.json', 'r') as f:
        # 提取出来是str类型
        browsers_json = json.load(f)
        # 转换成字典
        browsers_json = json.loads(browsers_json)
        # 下面都是取键值对操作
        browsers = browsers_json['browsers']
        # 判断浏览器
        num = random.randint(0, len(browsers))
        browsers_name = ''
        if num == 0:
            browsers_name = browsers['chrome']
        elif num == 1:
            browsers_name = browsers['opera']
        elif num == 2:
            browsers_name = browsers['firefox']
        elif num == 3:
            browsers_name = browsers['internetexplorer']
        else:
            browsers_name = browsers['safari']
        # browsers_name <class 'list'>
        return random.choice(browsers_name)

if __name__ == '__main__':
    # 将json文件下载到本地
    # get_user_agent_browsers()
    print(get_random_browsers())


