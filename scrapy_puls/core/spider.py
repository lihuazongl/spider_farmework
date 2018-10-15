from ..http_.request import Request
from ..item import Item

# 爬虫模块
# 1 构建原始请求
# 2 解析响应数据

class Spider(object):

    # 起始URL
    start_urls = 'https://www.baidu.com/'

    def start_request(self):
        """
        构建起始请求
        :return: 封装起始url ，传给请求对象进行请求
        """
        return Request(self.start_urls)

    def parse(self, response):
        """
        解析
        :param response:
        :return: 解析数据 传给item类进行封装
        """
        print(response.url)
        return Item(response.body)

