# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from scrapy_pro.items import MusicInfoItem

class TaiheSpider(scrapy.Spider):
    name = 'taihe'
    allowed_domains = ['music.taihe.com']

    # 获取316页包含歌单的页面
    def start_requests(self):
        for page in range(0, 316):
            url = 'http://music.taihe.com/songlist/' \
                   'tag/%E5%85%A8%E9%83%A8?orderType=1&' \
                   'offset={}&third_type='.format(page*20)
            req = scrapy.Request(url, callback=self.parse)
            yield req

    # 返回的所有歌单页，发送新请求获取歌单id
    def parse(self, response):
        pat = re.compile(r'<a href="(/songlist/.*?)" title=".*?">')
        music_list = pat.findall(response.text)
        base_url = 'http://music.taihe.com'
        for i in music_list:
            new_url = base_url+i
            req = scrapy.Request(new_url, callback=self.get_music_list)
            yield req

    # 由歌单页获取歌曲id
    def get_music_list(self, response):
        pat = re.compile(r'<a href="/song/(.*?)"')
        music_list = pat.findall(response.text)
        base_url = 'http://music.taihe.com/song/'
        for i in music_list:
            new_url = base_url + i
            req = scrapy.Request(new_url, callback=self.get_song_info)
            req.meta['id'] = i
            yield req

    # 返回的歌曲内容详情
    def get_song_info(self, response):
        res_ele = etree.HTML(response.text)
        item = MusicInfoItem()
        item['song_id'] = response.meta['id']
        item['song_name'] = res_ele.xpath('//div/div/h2/span/text()')[0]
        item['singer'] = res_ele.xpath('//div/p/span/span/a/text()')[0]
        item['zhuanji'] = res_ele.xpath('//div/p[2]/a/text()')[0]
        item['publish'] = res_ele.xpath('//div/p[3]/text()')[0].split('：')[-1]
        item['company'] = res_ele.xpath('//div/p[4]/text()')[0].split('：')[-1]

        yield item