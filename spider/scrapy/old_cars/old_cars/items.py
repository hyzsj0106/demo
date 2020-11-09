# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OldCarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class InfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 第一批26
    title = scrapy.Field()
    carid_uptime = scrapy.Field()
    kilometres = scrapy.Field()
    change_speed_box = scrapy.Field()
    car_transfer_num = scrapy.Field()
    year_survey_time = scrapy.Field()
    strong_danger = scrapy.Field()
    commerce_insurance = scrapy.Field()
    xinghao_name = scrapy.Field()
    changshang_name = scrapy.Field()
    jibie = scrapy.Field()
    fadongji = scrapy.Field()
    jiegou = scrapy.Field()
    lwh = scrapy.Field()
    zhoujv = scrapy.Field()
    xingli_rongji = scrapy.Field()
    zhiliang = scrapy.Field()
    pailiang = scrapy.Field()
    jinqi = scrapy.Field()
    qigang = scrapy.Field()
    mali = scrapy.Field()
    ranliao = scrapy.Field()
    qiyou = scrapy.Field()
    gongyou = scrapy.Field()
    pfbiaozhun = scrapy.Field()
    qdfangshi = scrapy.Field()
    # 第二批14
    Abs= scrapy.Field()
    zhidongyouguan= scrapy.Field()
    qianpaiceqinang= scrapy.Field()
    jiashiqinang= scrapy.Field()
    houpaiceqinang = scrapy.Field()
    houpaitouqinang = scrapy.Field()
    fujiashiqinang = scrapy.Field()
    qianpaitouqinang = scrapy.Field()
    no_key = scrapy.Field()
    taiya = scrapy.Field()
    child_zuoyi = scrapy.Field()
    center_key = scrapy.Field()
    yaokongkey = scrapy.Field()
    zhuchestop = scrapy.Field()
    # 第三批33
    houyushua = scrapy.Field()
    diandong_houbeixiang = scrapy.Field()
    diandong_xihemen = scrapy.Field()
    ganying_houbeixiang = scrapy.Field()
    houpai_cezheyang = scrapy.Field()
    zuoqian_lunyi = scrapy.Field()
    zuoqian_luntai = scrapy.Field()
    youqian_luntai = scrapy.Field()
    youhou_lunyi = scrapy.Field()
    zuohou_luntai = scrapy.Field()
    youqian_lunyi = scrapy.Field()
    zuohou_lunyi = scrapy.Field()
    youhou_luntai = scrapy.Field()
    tongzhou_huawen = scrapy.Field()
    tianchuang_boli = scrapy.Field()
    houbeixiang_statu = scrapy.Field()
    you_qianmen_boli = scrapy.Field()
    zuo_houmen_boli = scrapy.Field()
    cheliang_change = scrapy.Field()
    zhongwang = scrapy.Field()
    youhoumen_boli = scrapy.Field()
    youxianggai_statu = scrapy.Field()
    hou_fengdang_boli = scrapy.Field()
    youce_houshi = scrapy.Field()
    cheshen_waiguan = scrapy.Field()
    zuo_houshi = scrapy.Field()
    zuohoulunmei = scrapy.Field()
    yushua_penshuiqi = scrapy.Field()
    qian_fengdang_boli = scrapy.Field()
    zuoqianlunmei = scrapy.Field()
    youhoulunmei = scrapy.Field()
    youqianlunmei = scrapy.Field()
    zuoqianmenboli = scrapy.Field()
    # 第四批48
    vin = scrapy.Field()
    zhenkong_zhuli = scrapy.Field()
    diandong_zuoyi = scrapy.Field()
    zhongkongtai = scrapy.Field()
    duogongneng_fxp = scrapy.Field()
    daoche_yingxiang = scrapy.Field()
    zuoyi_tongfeng = scrapy.Field()
    daocheleida = scrapy.Field()
    hou_zheyanglian = scrapy.Field()
    hud_xianshi = scrapy.Field()
    qianpaizuoyi_hot = scrapy.Field()
    houpaizuoyi_hot = scrapy.Field()
    gps = scrapy.Field()
    kongtiaostatu = scrapy.Field()
    simenboli = scrapy.Field()
    tianchuang = scrapy.Field()
    audio_speaker = scrapy.Field()
    zuobzhu_trim = scrapy.Field()
    yibiaopan = scrapy.Field()
    fangxiangpanlaba = scrapy.Field()
    zuodzhu_trim = scrapy.Field()
    zuoczhu_trim = scrapy.Field()
    houbeixiang_trim = scrapy.Field()
    zuohoumen_trim = scrapy.Field()
    zuoqianmen_trim = scrapy.Field()
    youhoumen_trim = scrapy.Field()
    youqianmen_trim = scrapy.Field()
    youazhu_trim = scrapy.Field()
    zuoyi = scrapy.Field()
    youbzhu_trim = scrapy.Field()
    tianchuanzheyanglian = scrapy.Field()
    youdzhu_trim = scrapy.Field()
    anquandai = scrapy.Field()
    youczhu_trim = scrapy.Field()
    changpeng = scrapy.Field()
    kongtiaofengkou = scrapy.Field()
    shoutaoxiang = scrapy.Field()
    chemenkaiqistatu = scrapy.Field()
    houshijing = scrapy.Field()
    cheding_trim = scrapy.Field()
    zuoazhu_trim = scrapy.Field()
    zheyangban = scrapy.Field()
    ziqiting = scrapy.Field()
    quanjing = scrapy.Field()
    weixiubao = scrapy.Field()
    sanjiaobiao = scrapy.Field()
    beitai = scrapy.Field()
    qianjinding = scrapy.Field()
    url_referer = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO old_cars values (null,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s)'
        data = (
        self['title'], self['carid_uptime'], self['kilometres'], self['change_speed_box'],
        self['car_transfer_num'],self['year_survey_time'], self['strong_danger'],
        self['commerce_insurance'], self['xinghao_name'],self['changshang_name'],
        self['jibie'], self['fadongji'],self['jiegou'], self['lwh'], self['zhoujv'],
        self['xingli_rongji'],self['zhiliang'], self['pailiang'],self['jinqi'],
        self['qigang'],self['mali'],self['ranliao'], self['qiyou'], self['gongyou'],
        self['pfbiaozhun'], self['qdfangshi'],self['Abs'], self['zhidongyouguan'],
        self['qianpaiceqinang'],self['jiashiqinang'], self['houpaiceqinang'],
        self['houpaitouqinang'], self['fujiashiqinang'], self['qianpaitouqinang'],
        self['no_key'], self['taiya'], self['child_zuoyi'], self['center_key'],
        self['yaokongkey'], self['zhuchestop'],self['houyushua'],
        self['diandong_houbeixiang'],self['diandong_xihemen'],self['ganying_houbeixiang'],
        self['houpai_cezheyang'], self['zuoqian_lunyi'], self['zuoqian_luntai'],
        self['youqian_luntai'],self['youhou_lunyi'],self['zuohou_luntai'],
        self['youqian_lunyi'], self['zuohou_lunyi'], self['youhou_luntai'],
        self['tongzhou_huawen'],self['tianchuang_boli'],self['houbeixiang_statu'],
        self['you_qianmen_boli'], self['zuo_houmen_boli'], self['cheliang_change'],
        self['zhongwang'],self['youhoumen_boli'],self['youxianggai_statu'],
        self['hou_fengdang_boli'], self['youce_houshi'],self['cheshen_waiguan'],
        self['zuo_houshi'],self['zuohoulunmei'],self['yushua_penshuiqi'],
        self['qian_fengdang_boli'],self['zuoqianlunmei'], self['youhoulunmei'],
        self['youqianlunmei'],self['zuoqianmenboli'],self['vin'],self['zhenkong_zhuli'],
        self['diandong_zuoyi'],self['zhongkongtai'], self['duogongneng_fxp'],
        self['daoche_yingxiang'],self['zuoyi_tongfeng'], self['daocheleida'],
        self['hou_zheyanglian'],self['hud_xianshi'], self['qianpaizuoyi_hot'],
        self['houpaizuoyi_hot'], self['gps'], self['kongtiaostatu'],self['simenboli'],
        self['tianchuang'], self['audio_speaker'], self['zuobzhu_trim'], self['yibiaopan'],
        self['fangxiangpanlaba'],self['zuodzhu_trim'],self['zuoczhu_trim'],
        self['houbeixiang_trim'], self['zuohoumen_trim'], self['zuoqianmen_trim'],
        self['youhoumen_trim'],self['youqianmen_trim'],self['youazhu_trim'],
        self['zuoyi'], self['youbzhu_trim'], self['tianchuanzheyanglian'],
        self['youdzhu_trim'],self['anquandai'],self['youczhu_trim'], self['changpeng'],
        self['kongtiaofengkou'],self['shoutaoxiang'], self['chemenkaiqistatu'],
        self['houshijing'],self['cheding_trim'], self['zuoazhu_trim'],self['zheyangban'],
        self['ziqiting'], self['quanjing'],self['weixiubao'],self['sanjiaobiao'],
        self['beitai'],self['qianjinding'],self['url_referer'])

        return insert_sql, data


# CREATE TABLE IF NOT EXISTS old_cars(
# id int primary key AUTO_INCREMENT,
# title varchar(50),
# carid_uptime varchar(30),
# kilometres varchar(30),
# change_speed_box varchar(30),
# car_transfer_num varchar(10),
# year_survey_time varchar(30),
# strong_danger varchar(30),
# commerce_insurance varchar(30),
# xinghao_name varchar(30),
# changshang_name varchar(30),
# jibie varchar(10),
# fadongji varchar(30),
# jiegou varchar(30),
# lwh varchar(30),
# zhoujv varchar(30),
# xingli_rongji varchar(30),
# zhiliang varchar(30),
# pailiang varchar(30),
# jinqi varchar(30),
# qigang varchar(10),
# mali varchar(30),
# ranliao varchar(10),
# qiyou varchar(10),
# gongyou varchar(10),
# pfbiaozhun varchar(10),
# qdfangshi varchar(10),
# Abs varchar(30),
# zhidongyouguan varchar(30),
# qianpaiceqinang varchar(30),
# jiashiqinang varchar(30),
# houpaiceqinang varchar(30),
# houpaitouqinang varchar(30),
# fujiashiqinang varchar(30),
# qianpaitouqinang varchar(30),
# no_key varchar(30),
# taiya varchar(30),
# child_zuoyi varchar(30),
# center_key varchar(30),
# yaokongkey varchar(30),
# zhuchestop varchar(30),
# houyushua varchar(30),
# diandong_houbeixiang varchar(30),
# diandong_xihemen varchar(30),
# ganying_houbeixiang varchar(30),
# houpai_cezheyang varchar(30),
# zuoqian_lunyi varchar(30),
# zuoqian_luntai varchar(30),
# youqian_luntai varchar(30),
# youhou_lunyi varchar(30),
# zuohou_luntai varchar(30),
# youqian_lunyi varchar(30),
# zuohou_lunyi varchar(30),
# youhou_luntai varchar(30),
# tongzhou_huawen varchar(30),
# tianchuang_boli varchar(30),
# houbeixiang_statu varchar(30),
# you_qianmen_boli varchar(30),
# zuo_houmen_boli varchar(30),
# cheliang_change varchar(30),
# zhongwang varchar(30),
# youhoumen_boli varchar(30),
# youxianggai_statu varchar(30),
# hou_fengdang_boli varchar(30),
# youce_houshi varchar(30),
# cheshen_waiguan varchar(30),
# zuo_houshi varchar(30),
# zuohoulunmei varchar(30),
# yushua_penshuiqi varchar(30),
# qian_fengdang_boli varchar(30),
# zuoqianlunmei varchar(30),
# youhoulunmei varchar(30),
# youqianlunmei varchar(30),
# zuoqianmenboli varchar(30),
# vin varchar(30),
# zhenkong_zhuli varchar(30),
# diandong_zuoyi varchar(30),
# zhongkongtai varchar(30),
# duogongneng_fxp varchar(30),
# daoche_yingxiang varchar(30),
# zuoyi_tongfeng varchar(30),
# daocheleida varchar(30),
# hou_zheyanglian varchar(30),
# hud_xianshi varchar(30),
# qianpaizuoyi_hot varchar(30),
# houpaizuoyi_hot varchar(30),
# gps varchar(30),
# kongtiaostatu varchar(30),
# simenboli varchar(30),
# tianchuang varchar(30),
# audio_speaker varchar(30),
# zuobzhu_trim varchar(30),
# yibiaopan varchar(30),
# fangxiangpanlaba varchar(30),
# zuodzhu_trim varchar(30),
# zuoczhu_trim varchar(30),
# houbeixiang_trim varchar(30),
# zuohoumen_trim varchar(30),
# zuoqianmen_trim varchar(30),
# youhoumen_trim varchar(30),
# youqianmen_trim varchar(30),
# youazhu_trim varchar(30),
# zuoyi varchar(30),
# youbzhu_trim varchar(30),
# tianchuanzheyanglian varchar(30),
# youdzhu_trim varchar(30),
# anquandai varchar(30),
# youczhu_trim varchar(30),
# changpeng varchar(30),
# kongtiaofengkou varchar(30),
# shoutaoxiang varchar(30),
# chemenkaiqistatu varchar(30),
# houshijing varchar(30),
# cheding_trim varchar(30),
# zuoazhu_trim varchar(30),
# zheyangban varchar(30),
# ziqiting varchar(30),
# quanjing varchar(30),
# weixiubao varchar(30),
# sanjiaobiao varchar(30),
# beitai varchar(30),
# qianjinding varchar(30),
# url_referer varchar(100)
# )DEFAULT CHARSET='utf8mb4';
