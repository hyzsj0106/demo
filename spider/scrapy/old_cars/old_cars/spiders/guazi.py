# -*- coding: utf-8 -*-
import scrapy
import re
from urllib import parse
from old_cars.items import InfoItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    # 创建初始链接
    def start_requests(self):
        city_list = ['sy','fushun','anshan','liaoyang','dl','jinzhou','yingkou']
        cookies = {
            'antipas': '此处内容省略',
            'uuid': '此处内容省略',
            'ganji_uuid': '此处内容省略',
            'clueSourceCode': '此处内容省略',
            'guazitrackersessioncadata': '此处内容省略',
            'sessionid': '此处内容省略',
            'lg': '1',
            'cainfo': '此处内容省略',
            '_gl_tracker': '此处内容省略',
            'preTime': '此处内容省略',
        }
        # 遍历城市列表分别访问
        for city in city_list:
            for page in range(1, 51):
                request_url = 'https://www.guazi.com/{}/buy/o{}'.format(city,page)
                # request_url = 'https://www.guazi.com/sy/buy/o1'
                req = scrapy.Request(request_url,callback=self.parse,cookies=cookies)
                req.meta['referer'] = request_url
                req.meta['cookies'] = cookies

                yield req


    def parse(self, response):
        # 保存查看返回的response,用于匹配对应数据
        # with open('guazi.html','w',encoding='utf-8') as f:
        #     f.write(response.text)
        page_info_url_list = re.findall('<a title=".*?" href="(.*?)" target="_blank"',
                                        response.text)
        for page_url in page_info_url_list:
            referer_url = response.meta['referer']
            cookies = response.meta['cookies']
            page_info_url = parse.urljoin(referer_url, page_url)
            req = scrapy.Request(page_info_url, callback=self.page_info,
                                 cookies=cookies)
            req.meta['url_referer'] = page_info_url

            yield req

    def page_info(self,response):
        # 保存网页查看本地匹配
        # with open('page_info.html','w',encoding='utf-8')as f:
        #     f.write(response.text)
        item = InfoItem()
    # 基本信息
        # 获取对应链接地址
        item['url_referer'] = response.meta['url_referer']
        # 获取标题
        item['title'] = response.xpath(
            "/html/body/div[4]/div[3]/div[2]/h2/text()").extract_first()
        # 上牌时间
        item['carid_uptime'] = self.panduan_none_list(re.findall(
            '<li class="one"><span>(.*?)</span>上牌时间</li>', response.text))
        # 里程数
        item['kilometres'] = self.panduan_none_list(re.findall(
            '<li class="two"><span>(.*?)</span>表显里程</li>', response.text))
        # 变速箱(自动还是手动)
        item['change_speed_box'] = self.panduan_none_list(re.findall(
            '<li class="last"><span>(.*?)</span>变速箱</li>', response.text))
        # 过户次数
        item['car_transfer_num'] = self.panduan_none_list(re.findall(
            '<div class="typebox">(\d)次过户',response.text))
        # 年检到期时间
        item['year_survey_time'] = self.panduan_none_list(re.findall(
            '<li class="nine"><div class="typebox">(.*?)</div>年检到期</li>',
            response.text))
        # 强险
        item['strong_danger'] = self.panduan_none_list(re.findall(
            '<li class="ten"><div class="typebox">(.*?)</div>交强险</li>',response.text))
        # 商业险
        item['commerce_insurance'] = self.panduan_none_list(re.findall(
            'class="typebox">(.*?)<span class=".*?js-tip-icon4"', response.text))
        # 证件品牌型号
        item['xinghao_name'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[2]/td[2]/"
            "text()").extract_first()
        # 厂商名
        item['changshang_name'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[3]/td[2]/"
            "text()").extract_first()
        # 级别
        item['jibie'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[3]/td[2]/"
            "text()").extract_first()
        # 发动机
        item['fadongji'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[4]/td[2]/"
            "text()").extract_first()
        # 车身结构
        item['jiegou'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[6]/td[2]/"
            "text()").extract_first()
        # 长宽高
        item['lwh'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[7]/td[2]/"
            "text()").extract_first()
        # 轴距
        item['zhoujv'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[8]/td[2]/"
            "text()").extract_first()
        # 行李箱容积
        item['xingli_rongji'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[9]/td[2]/"
            "text()").extract_first()
        # 整备质量
        item['zhiliang'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[1]//tr[10]/td[2]/"
            "text()").extract_first()
        # 排量
        item['pailiang'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[2]/td[2]/"
            "text()").extract_first()
        # 进气形式
        item['jinqi'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[3]/td[2]/"
            "text()").extract_first()
        # 气缸
        item['qigang'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[4]/td[2]/"
            "text()").extract_first()
        # 最大马力
        item['mali'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[5]/td[2]/"
            "text()").extract_first()
        # 燃料
        item['ranliao'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[7]/td[2]/"
            "text()").extract_first()
        # 汽油编号
        item['qiyou'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[8]/td[2]/"
            "text()").extract_first()
        # 供油方式
        item['gongyou'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[9]/td[2]/"
            "text()").extract_first()
        # 排放标准
        item['pfbiaozhun'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[2]//tr[10]/td[2]"
            "/text()").extract_first()
        # 驱动方式
        item['qdfangshi'] = response.xpath(
            "//div[@class='basic-infor js-basic-infor js-top']/div/table[3]//tr[2]/td[2]/"
            "text()").extract_first()
    # re正则匹配(因为这些监测项目的顺序不固定,xpath匹配会出很多问题)
    # 14项安全系统检测
        item['Abs'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*ABS泵', response.text))
        item['zhidongyouguan'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*制动油管', response.text))
        item['qianpaiceqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*前排侧气囊', response.text))
        item['jiashiqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*驾驶座安全气囊', response.text))
        item['houpaiceqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后排侧气囊',response.text))
        item['houpaitouqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后排头部气囊', response.text))
        item['fujiashiqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*副驾驶安全气囊', response.text))
        item['qianpaitouqinang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*前排头部气囊', response.text))
        item['no_key'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*无钥匙启动', response.text))
        item['taiya'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*胎压监测', response.text))
        item['child_zuoyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*儿童座椅接口', response.text))
        item['center_key'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*中控锁', response.text))
        item['yaokongkey'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*遥控钥匙', response.text))
        item['zhuchestop'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*驻车制动', response.text))

    # 33项外部配置检测
        item['houyushua'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后雨刷',response.text))
        item['diandong_houbeixiang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*电动后备箱',response.text))
        item['diandong_xihemen'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*电动吸合门',response.text))
        item['ganying_houbeixiang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*感应后备箱',response.text))
        item['houpai_cezheyang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后排侧遮阳帘',response.text))
        item['zuoqian_lunyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左前轮毂',response.text))
        item['zuoqian_luntai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左前轮胎',response.text))
        item['youqian_luntai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右前轮胎',response.text))
        item['youhou_lunyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右后轮毂',response.text))
        item['zuohou_luntai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左后轮胎',response.text))
        item['youqian_lunyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右前轮毂',response.text))
        item['zuohou_lunyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左后轮毂',response.text))
        item['youhou_luntai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右后轮胎',response.text))
        item['tongzhou_huawen'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*同轴花纹一致',response.text))
        item['tianchuang_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*天窗玻璃',response.text))
        item['houbeixiang_statu'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后备箱开启状态',response.text))
        item['you_qianmen_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右前门玻璃',response.text))
        item['zuo_houmen_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左后门玻璃',response.text))
        item['cheliang_change'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*车辆改装',response.text))
        item['zhongwang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*中网',response.text))
        item['youhoumen_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右后门玻璃',response.text))
        item['youxianggai_statu'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*油箱盖开启状态',response.text))
        item['hou_fengdang_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后风挡玻璃',response.text))
        item['youce_houshi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右侧后视镜',response.text))
        item['cheshen_waiguan'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*车身外观',response.text))
        item['zuo_houshi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左侧后视镜',response.text))
        item['zuohoulunmei'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左后轮眉',response.text))
        item['yushua_penshuiqi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*雨刷及喷水器',response.text))
        item['qian_fengdang_boli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*前风挡玻璃',response.text))
        item['zuoqianlunmei'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左前轮眉',response.text))
        item['youhoulunmei'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右后轮眉',response.text))
        item['youqianlunmei'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右前轮眉',response.text))
        item['zuoqianmenboli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左前门玻璃',response.text))

    # 42项内部配置检测

        item['vin'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*VIN码',response.text))
        item['zhenkong_zhuli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*真空助力泵',response.text))
        item['diandong_zuoyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*驾驶座座椅电动调节',response.text))
        item['zhongkongtai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*中控台',response.text))
        item['duogongneng_fxp'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*多功能方向盘',response.text))
        item['daoche_yingxiang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*倒车影像系统',response.text))
        item['zuoyi_tongfeng'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*座椅通风',response.text))
        item['daocheleida'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*倒车雷达',response.text))
        item['hou_zheyanglian'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后风挡遮阳帘',response.text))
        item['hud_xianshi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*HUD抬头显示',response.text))
        item['qianpaizuoyi_hot'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*前排座椅加热',response.text))
        item['houpaizuoyi_hot'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后排座椅加热',response.text))
        item['gps'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*GPS导航',response.text))
        item['kongtiaostatu'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*空调状态',response.text))
        item['simenboli'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*四门玻璃启动',response.text))
        item['tianchuang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*天窗.*?启动',response.text))
        item['audio_speaker'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*音响扬声器',response.text))
        item['zuobzhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左B柱内饰板',response.text))
        item['yibiaopan'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*仪表盘',response.text))
        item['fangxiangpanlaba'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*方向盘喇叭',response.text))
        item['zuodzhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左D柱内饰板',response.text))
        item['zuoczhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左C柱内饰板',response.text))
        item['houbeixiang_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*后备箱饰板',response.text))
        item['zuohoumen_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左后门内饰板',response.text))
        item['zuoqianmen_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左前门内饰板',response.text))
        item['youhoumen_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右后门内饰板',response.text))
        item['youqianmen_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右前门内饰板',response.text))
        item['youazhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右A柱内饰板',response.text))
        item['zuoyi'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*座椅',response.text))
        item['youbzhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右B柱内饰板',response.text))
        item['tianchuanzheyanglian'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*天窗遮阳帘',response.text))
        item['youdzhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右D柱内饰板',response.text))
        item['anquandai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*安全带',response.text))
        item['youczhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*右C柱内饰板',response.text))
        item['changpeng'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*敞篷',response.text))
        item['kongtiaofengkou'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*空调出风口',response.text))
        item['shoutaoxiang'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*手套箱',response.text))
        item['chemenkaiqistatu'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*车门开启状态',response.text))
        item['houshijing'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*车内后视镜',response.text))
        item['cheding_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*车顶内饰板',response.text))
        item['zuoazhu_trim'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*左A柱内饰板',response.text))
        item['zheyangban'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*遮阳板',response.text))

        # 2项高科技配置检测
        item['ziqiting'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*发动机自动启停', response.text))
        item['quanjing'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*全景摄像头', response.text))

        # 4项随车工具检测
        item['weixiubao'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*维修工具包', response.text))
        item['sanjiaobiao'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*三角警示标', response.text))
        item['beitai'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*备胎', response.text))
        item['qianjinding'] = self.panduan_none_list(re.findall(
            '<span class="(.*?)">\s*</span>\s*千斤顶', response.text))

        yield item

    def panduan_none_list(self,res):
        result = []
        if len(res) != 0:
            result = res[0].strip()
        else:
            result = None
        return result
