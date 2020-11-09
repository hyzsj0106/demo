# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MusicInfoItem(scrapy.Item):
    song_id = scrapy.Field()
    song_name = scrapy.Field()
    singer = scrapy.Field()
    zhuanji = scrapy.Field()
    publish = scrapy.Field()
    company = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO taihemusic (id, song_name, ' \
                     'singer, zhuanji, publish, company) ' \
                     'VALUES(%s, %s, %s, %s, %s, %s)'
        data = (self['song_id'], self['song_name'], self['singer'],
                self['zhuanji'], self['publish'], self['company'])

        return insert_sql, data


# create table if not exists taihemusic(
# id int,
# song_name varchar(100),
# singer varchar(50),
# zhuanji varchar(100),
# publish varchar(50),
# company varchar(50)
# )default charset='utf8mb4';