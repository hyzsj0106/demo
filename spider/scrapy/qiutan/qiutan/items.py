# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiutanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SaichengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lunci = scrapy.Field()
    bs_num_id = scrapy.Field()
    bs_time = scrapy.Field()
    host_team = scrapy.Field()
    h_team_id = scrapy.Field()
    res_score = scrapy.Field()
    guest_team = scrapy.Field()
    g_team_id = scrapy.Field()
    all_rang = scrapy.Field()
    half_rang = scrapy.Field()
    sizes_balls_a = scrapy.Field()
    sizes_balls_h = scrapy.Field()
    half_score = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_bs_data values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['lunci'], self['bs_num_id'], self['bs_time'], self['host_team'], self['h_team_id'], self['res_score'],
        self['guest_team'],
        self['g_team_id'], self['all_rang'], self['half_rang'], self['sizes_balls_a'], self['sizes_balls_h'],
        self['half_score'])

        return insert_sql, data


# all_bs_data 建表语句
# CREATE TABLE all_bs_data(id INT PRIMARY KEY AUTO_INCREMENT,
# lunci TINYINT,
# bs_time VARCHAR(20),
# host_team VARCHAR(20),
# h_team_id VARCHAR(6),
# res_score VARCHAR(10),
# guest_team VARCHAR(20),
# g_team_id VARCHAR(6),
# all_rang VARCHAR(6),
# half_rang VARCHAR(6),
# sizes_balls_a VARCHAR6),
# sizes_balls_h VARCHAR(6),
# half_score VARCHAR(6)
# )DEFAULT CHARSET=utf8mb4;
# alter table all_bs_data add bs_num_id int after lunci;


class Team_DataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    team_id = scrapy.Field()
    team_name = scrapy.Field()
    Eng_name = scrapy.Field()
    team_city = scrapy.Field()
    team_home = scrapy.Field()
    build_team_time = scrapy.Field()
    var_coach = scrapy.Field()
    team_youshi = scrapy.Field()
    team_style = scrapy.Field()
    team_ruodian = scrapy.Field()
    team_stats = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_team_data(team_id,team_name,Eng_name,team_city,team_home,build_team_time,var_coach,team_youshi,team_style,team_ruodian,team_stats)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['team_id'], self['team_name'], self['Eng_name'], self['team_city'], self['team_home'],
                self['build_team_time'],
                self['var_coach'], self['team_youshi'], self['team_style'], self['team_ruodian'], self['team_stats'])

        return insert_sql, data


# CREATE TABLE all_team_data(id INT PRIMARY KEY AUTO_INCREMENT,
# team_id INT,
# team_name VARCHAR(20),
# Eng_name VARCHAR(30),
# team_city VARCHAR(30),
# team_home VARCHAR(30),
# build_team_time VARCHAR(20),
# var_coach VARCHAR(20),
# team_youshi VARCHAR(200),
# team_style VARCHAR(200),
# team_ruodian VARCHAR(200),
# team_stats VARCHAR(300)
# )DEFAULT CHARSET=utf8mb4;

class Member_Data_New_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bs_num_id = scrapy.Field()
    team_id = scrapy.Field()
    member_id = scrapy.Field()
    member_name = scrapy.Field()
    position = scrapy.Field()
    shoot_d = scrapy.Field()
    shoot_z = scrapy.Field()
    key_ball = scrapy.Field()
    guoren = scrapy.Field()
    chuanq_count = scrapy.Field()
    chuanq_succ = scrapy.Field()
    passing = scrapy.Field()
    hengchuanc = scrapy.Field()
    success_zd = scrapy.Field()
    body_jc = scrapy.Field()
    score = scrapy.Field()
    key_event = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_member_data values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['bs_num_id'], self['team_id'], self['member_id'], self['member_name'], self['position'], self['shoot_d'],
        self['shoot_z'], self['key_ball'], self['guoren'], self['chuanq_count'], self['chuanq_succ'], self['passing']
        , self['hengchuanc'], self['success_zd'], self['body_jc'], self['score'], self['key_event'])

        return insert_sql, data


# CREATE TABLE all_member_data(id INT PRIMARY KEY AUTO_INCREMENT,
# bs_num_id INT,
# team_id INT,
# member_id INT,
# member_name VARCHAR(30),
# position VARCHAR(10),
# shoot_d INT,
# shoot_z INT,
# key_ball INT,
# guoren INT,
# chuanq_count INT,
# chuanq_succ INT,
# passing VARCHAR(200),
# hengchuanc INT,
# success_zd INT,
# body_jc INT,
# score FLOAT,
# key_event VARCHAR(20)
# )DEFAULT CHARSET=utf8mb4;

class Member_Data_Old_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bs_num_id = scrapy.Field()
    team_id = scrapy.Field()
    member_id = scrapy.Field()
    member_name = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_member_data(bs_num_id,team_id,member_id,member_name) values (%s,%s,%s,%s)'
        data = (self['bs_num_id'], self['team_id'], self['member_id'], self['member_name'])

        return insert_sql, data