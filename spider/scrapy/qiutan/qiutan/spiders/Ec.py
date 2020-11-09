# -*- coding: utf-8 -*-
import scrapy
import re, time
from qiutan.items import SaichengItem
from qiutan.items import Team_DataItem
from qiutan.items import Member_Data_New_Item
from qiutan.items import Member_Data_Old_Item


class EcSpider(scrapy.Spider):
    name = 'Ec'
    allowed_domains = ['zq.win007.com', 'bf.win007.com']

    # 将不同年份url交给Scheduler
    def start_requests(self):
        re = time.strftime('%Y%m%d%H', time.localtime())  # 2019042509
        base_url = 'http://zq.win007.com/jsData/matchResult/{}/s36.js?version={}'
        date_lis = ['{}-{}'.format(i, i + 1) for i in range(2013, 2019)]
        for date in date_lis:
            req_base = scrapy.Request(base_url.format(date, re), callback=self.parse)
            req_base.meta['date'] = date
            req_base.meta['re'] = re
            yield req_base

    def team_data_id(self, response):
        # 获取每个队伍的id和队名
        pat = re.compile("\[(\d+),'(.*?)'")
        ballteam = pat.findall(response.text)[1:]
        lis_all_team = []
        for item in ballteam:
            lis_all_team.append(item[0])
            lis_all_team.append(item[-1])
        return lis_all_team

    # 表2 全部轮次的数据表
    def parse(self, response):
        # 获取球队id_队名列表
        lis_all_team = self.team_data_id(response)
        # 获取每年所有队伍数据 38轮
        ball_lunci_team = re.findall('\[(\[\d{3,}.*?\])\];', response.text)
        num = 0
        # 根据38轮遍历每一小轮
        for eve_turn in ball_lunci_team:
            # 每小页数据
            item = SaichengItem()
            num += 1
            # 每轮次的10条数据
            eve_turn_team = re.findall('\[\d{6}.*?\]', eve_turn)
            for eve_turn_team_data in eve_turn_team:
                # 将每行数据转化为list类型 索引取值
                # [851543,36,-1,'2013-08-17 19:45',25,58,'1-0','1-0','7',
                # '13',1.25,0.5,'2.5/3','1',1,1,1,1,0,0,'']
                lis = eve_turn_team_data.strip('[|]').replace('\'', '').split(',')
                # 根据获取的战队id去之前的列表找索引位置
                index_num_h = lis_all_team.index(lis[4])
                index_num_g = lis_all_team.index(lis[5])
                item['lunci'] = num
                bs_num_id = lis[0]
                item['bs_time'] = lis[3]  # 2014-05-04 23:00 <class 'str'>
                item['bs_num_id'] = bs_num_id
                item['host_team'] = lis_all_team[index_num_h + 1]
                item['h_team_id'] = lis[4]
                item['res_score'] = lis[6]
                item['guest_team'] = lis_all_team[index_num_g + 1]
                item['g_team_id'] = lis[5]
                item['all_rang'] = self.rangqiu(lis[10])
                item['half_rang'] = self.rangqiu(lis[11])
                item['sizes_balls_a'] = lis[12]
                item['sizes_balls_h'] = lis[13]
                item['half_score'] = lis[7]
                yield item
                # 拼接每个比赛详细的url http://bf.win007.com/detail/ 1130517 cn.htm
                # 2013-08-17 ,2014-5-12 老版页面  判断年份 保存版本
                if item['bs_time'] < '2014-05-12 0:00':
                    url = 'http://bf.win007.com/detail/{}cn.htm'.format(bs_num_id)
                    req = scrapy.Request(url, callback=self.bs_data_old)
                    req.meta['bs_num_id'] = bs_num_id
                    req.meta['l_team_id'] = lis[4]
                    req.meta['r_team_id'] = lis[5]
                    yield req

                else:
                    url = 'http://bf.win007.com/Count/{}cn.htm'.format(bs_num_id)
                    req = scrapy.Request(url, callback=self.bs_data_new)
                    req.meta['bs_num_id'] = bs_num_id
                    req.meta['l_team_id'] = lis[4]
                    req.meta['r_team_id'] = lis[5]
                    yield req

        team_url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/tdl{}.js?version={}'
        # 根据 偶数索引 取 球队id
        for i in range(len(lis_all_team)):
            if i % 2 == 0:
                url = team_url.format(lis_all_team[i], response.meta['re'])
                req = scrapy.Request(url, callback=self.team_data)
                # 加上防盗链获取接口
                req.meta['Referer'] = 'http://zq.win007.com/cn/team/Summary/{}.html'.format(lis_all_team[i])
                yield req

    # 每场比赛队员数据: 新版
    def bs_data_new(self, response):
        # 实例化Item
        item = Member_Data_New_Item()
        # 分别 取上下两个队伍的信息
        member_lis_tr_s = response.xpath('//div[@id="content"]/div[3]/table//tr[position()>2]')
        member_lis_tr_x = response.xpath('//div[@id="content"]/div[4]/table//tr[position()>2]')
        for member_lis in member_lis_tr_s:
            item['bs_num_id'] = response.meta['bs_num_id']
            item['team_id'] = response.meta['l_team_id']
            item['member_id'] = member_lis.xpath('./td[1]/text()').extract_first()
            item['member_name'] = member_lis.xpath('./td[2]/a//text()').extract_first().strip()
            item['position'] = member_lis.xpath('./td[3]/text()').extract_first().strip()
            item['shoot_d'] = member_lis.xpath('./td[4]/text()').extract_first()
            item['shoot_z'] = member_lis.xpath('./td[5]/text()').extract_first()
            item['key_ball'] = member_lis.xpath('./td[6]/text()').extract_first()
            item['guoren'] = member_lis.xpath('./td[7]/text()').extract_first()
            item['chuanq_count'] = member_lis.xpath('./td[8]/text()').extract_first()
            item['chuanq_succ'] = member_lis.xpath('./td[9]/text()').extract_first()
            item['passing'] = member_lis.xpath('./td[10]/text()').extract_first()
            item['hengchuanc'] = member_lis.xpath('./td[11]/text()').extract_first()
            item['success_zd'] = member_lis.xpath('./td[17]/text()').extract_first()
            item['body_jc'] = member_lis.xpath('./td[18]/text()').extract_first()
            item['score'] = member_lis.xpath('./td[30]/text()').extract_first()
            item['key_event'] = member_lis.xpath('./td[31]/a/img/@title').extract_first()
            yield item

        for member_lis in member_lis_tr_x:
            item['bs_num_id'] = response.meta['bs_num_id']
            item['team_id'] = response.meta['r_team_id']
            item['member_id'] = member_lis.xpath('./td[1]/text()').extract_first()
            item['member_name'] = member_lis.xpath('./td[2]/a/text()').extract_first().strip()
            item['position'] = member_lis.xpath('./td[3]/text()').extract_first().strip()
            item['shoot_d'] = member_lis.xpath('./td[4]/text()').extract_first()
            item['shoot_z'] = member_lis.xpath('./td[5]/text()').extract_first()
            item['key_ball'] = member_lis.xpath('./td[6]/text()').extract_first()
            item['guoren'] = member_lis.xpath('./td[7]/text()').extract_first()
            item['chuanq_count'] = member_lis.xpath('./td[8]/text()').extract_first()
            item['chuanq_succ'] = member_lis.xpath('./td[9]/text()').extract_first()
            item['passing'] = member_lis.xpath('./td[10]/text()').extract_first()
            item['hengchuanc'] = member_lis.xpath('./td[11]/text()').extract_first()
            item['success_zd'] = member_lis.xpath('./td[17]/text()').extract_first()
            item['body_jc'] = member_lis.xpath('./td[18]/text()').extract_first()
            item['score'] = member_lis.xpath('./td[30]/text()').extract_first()
            item['key_event'] = member_lis.xpath('./td[31]/a/img/@title').extract_first()

            yield item

    def bs_data_old(self, response):
        # 获取13年左边的阵容数据和后备数据,返回列表[含字符串,]
        member_lis_l1 = response.xpath("/html/body/table[1]/tr[1]/td[1]/table/tr[3]/td/a//text()").extract()
        member_lis_l2 = response.xpath("/html/body/table[1]/tr[1]/td[1]/table/tr[5]/td/a/text()").extract()
        # 获取13年右边的阵容数据和后备数据
        member_lis_r1 = response.xpath("/html/body/table[1]/tr[1]/td[3]/table/tr[3]/td/a/text()").extract()
        member_lis_r2 = response.xpath("/html/body/table[1]/tr[1]/td[3]/table/tr[5]/td/a/text()").extract()
        item = Member_Data_Old_Item()

        # 将阵容和后备列表合并
        member_lis_l = member_lis_l1 + member_lis_l2
        member_lis_r = member_lis_r1 + member_lis_r2
        # 遍历每个元组(球员号,球员名字)
        for member in member_lis_l:
            res = member.strip()
            member_list = re.findall('(\d+)\s?(.*)', res)[0]  # ('22', '雅斯科莱宁') ('11', '麦加')
            item['bs_num_id'] = response.meta['bs_num_id']
            item['team_id'] = response.meta['l_team_id']
            item['member_id'] = member_list[0]
            item['member_name'] = member_list[1]

            yield item

        for member in member_lis_r:
            res = member.strip()  # 1  切赫
            member_list = re.findall('(\d+)\s+(.*)', res)[0]  # ('17', '奥布莱恩')
            item['bs_num_id'] = response.meta['bs_num_id']
            item['team_id'] = response.meta['r_team_id']
            item['member_id'] = member_list[0]
            item['member_name'] = member_list[1]
            yield item

    # 球队信息
    def team_data(self, response):
        # 第一行数据
        teamDetail = re.findall('var teamDetail = \[(\d+.*)\]', response.text)
        teamDetail_lis = eval(teamDetail[0])
        # 获取教练
        var_coach = re.findall("var coach = \[\['\d+','','(.*?)','.*','.*',\d\]\];", response.text)
        item = Team_DataItem()
        #
        item['team_id'] = teamDetail_lis[0]
        item['team_name'] = teamDetail_lis[1]
        item['Eng_name'] = teamDetail_lis[3]
        item['team_city'] = teamDetail_lis[5]
        item['team_home'] = teamDetail_lis[8]
        item['build_team_time'] = teamDetail_lis[12]
        try:
            item['var_coach'] = var_coach[0]
        except:
            item['var_coach'] = 'NULL'

        # 球队特点
        item['team_youshi'] = str(re.findall('\[1,\d,"(.*?)\^', response.text))
        item['team_ruodian'] = str(re.findall('\[2,\d,"(.*?)\^', response.text))
        item['team_style'] = str(re.findall('\[3,\d,"(.*?)\^', response.text))
        team_stats_lis = re.findall('var countSum = \[\[(\'.*?)\]', response.text)[0]
        stats_tuple = eval(team_stats_lis)

        s = stats_tuple

        winrate = int(s[2]) / (int(s[2]) + int(s[3]) + int(s[4]))
        data = (s[2], s[3], s[4], winrate, s[5], s[6], s[7], s[8], s[9], (s[10]), s[11], (s[12]), s[13], s[14], s[24])
        str_stats = '全部:胜:%s,平:%s,负:%s,胜率:%.3f,犯规:%s,黄牌:%s,红牌:%s,' \
                    '控球率:%s,射门(射正):%s(%s),传球(成功):%s(%s),传球成功率:%s,过人次数:%s,评分:%s'
        item['team_stats'] = str_stats % (data)
        yield item

    def rangqiu(self, num_rang):
        if num_rang == '0':
            return '平手'
        elif num_rang == '0.25':
            return '平/半'
        elif num_rang == '0.5':
            return '半球'
        elif num_rang == '0.75':
            return '半/一'
        elif num_rang == '1':
            return '一球'
        elif num_rang == '1.25':
            return '一/球半'
        elif num_rang == '1.5':
            return '球半'
        elif num_rang == '1.75':
            return '半/二'
        elif num_rang == '2':
            return '二球'
        elif num_rang == '2.25':
            return '二/半'
        elif num_rang == '-0.25':
            return '*平/半'
        elif num_rang == '-0.5':
            return '*半球'
        elif num_rang == '-0.75':
            return '*半/一'
        elif num_rang == '-1':
            return '*一球'
        elif num_rang == '-1.25':
            return '*一/球半'
        elif num_rang == '-1.5':
            return '*球半'
        else:
            return '暂未收录'