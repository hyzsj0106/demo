import time
from io import BytesIO
from selenium.webdriver import ActionChains
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from requests_dir.ChaoJiying import Chaojiying
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'admin'
PASSWORD = 'admin'
CHAOJIYING_USERNAME = ''
CHAOJIYING_PASSWORD = ''
CHAOJIYING_SOFT_ID = 904673
CHAOJIYING_KIND = 9004
MULTIPLE = 1.25
if not CHAOJIYING_USERNAME or not CHAOJIYING_PASSWORD:
    print('请设置用户名和密码')
    exit(0)


class CreakCaptcha(object):
    def __init__(self):
        self.url = 'https://captcha3.scrape.cuiqingcai.com/'
        self.browser = webdriver.Chrome()
        self.username = USERNAME
        self.password = PASSWORD
        self.wait = WebDriverWait(self.browser, 20)
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME,
                                     CHAOJIYING_PASSWORD,
                                     CHAOJIYING_SOFT_ID)

    def open(self):
        """
        打开网页输入用户名密码,并点击按钮
        :return: None
        """
        self.browser.get(self.url)
        #  填入用户名密码
        username = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        password = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        # 点击按钮
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()

    def get_captcha_element(self):
        """
        获取验证图片对象
        :return: 图片对象
        """
        #  验证码图片加载出来
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'img.geetest_item_img')))
        #  验证码完整节点
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_widget')))
        print('成功获取验证码节点')
        return element

    def get_captcha_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        element = self.get_captcha_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], \
                                   location['x'], location['x'] + size['width']
        return (top * MULTIPLE, bottom * MULTIPLE, left * MULTIPLE, right * MULTIPLE)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        screenshot.save('screenshot.png')
        return screenshot

    def get_captcha_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_captcha_position()
        print('验证码实际位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        print('正在切割验证码')
        return captcha

    def post_captcha(self):
        '''
        发送截图到打码平台，接收结果
        :return:
        '''
        image = self.get_captcha_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        # 识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        return result
        # {'err_no': 0, 'err_str': 'OK', 'pic_id': '3102613224144800001',
        # 'pic_str': '247,373|196,250', 'md5': '6cf8d323538a3088bd72dafcac86d3c8'}

    def get_points(self):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        self.captcha_result = self.post_captcha()
        pic_str = self.captcha_result.get('pic_str')
        print(pic_str)
        groups = pic_str.split('|')
        locations = [[int(number) / MULTIPLE for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self):
        """
        点击验证图片
        :param locations: 点击位置
        :return: None
        """
        try:
            locations = self.get_points()
            element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'geetest_widget')))
            for location in locations:
                print('location 定位依次:', location)
                ActionChains(self.browser).move_to_element_with_offset(
                    element, location[0], location[1]).click().perform()
                time.sleep(1)
            self.browser.find_element(By.CLASS_NAME,'geetest_commit').click()
            self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), '登录成功'))
            print('登陆成功')

        except:
            error_result = self.chaojiying.report_error(self.captcha_result.get('pic_id'))
            print(error_result)
            print('Try again')
            ck.touch_click_words()


if __name__ == '__main__':
    ck = CreakCaptcha()
    ck.open()
    ck.touch_click_words()
    ck.browser.close()
