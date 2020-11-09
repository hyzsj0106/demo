import requests
import time


class ProxyHelper():
    def __init__(self):
        self.url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=9acd574101fc407c9d776d60a45219df&count=1&expiryDate=0&format=2&newLine=2'
        self.version = 0
        self.proxy = self.update_proxy(self.version)


    def get_proxy(self):

        return 'http://' + self.proxy, self.version

    # 使用version是因为多个进程可能同时需要更新一个代理, 其中有一个更新成功了
    # 其它的进程就不需要更新, 以免浪费代理ip
    def update_proxy(self, version):
        if version == self.version:

            response = requests.get(self.url)
            self.proxy = response.text.strip()
            self.version += 1
            print('更新了一个代理, 代理是: ' + self.proxy)
        return self.proxy

if __name__ == '__main__':
    helper = ProxyHelper()
    proxy, version = helper.get_proxy()
    print(proxy)

    time.sleep(30)

    helper.update_proxy(version)
    print(helper.get_proxy())