# 引擎模块
# 1 负责各个模块之间的调度
# 2 各个模块的数据传递


"""
实现思路
1 init方法中实例各个模块对象
2 提供一个接口对外请求引擎的方法start
3 提供一个私有的启动引擎的方法，用于实现核心逻辑

"""
from scrapy_puls.core.downloader import Downloader
from scrapy_puls.core.pipeline import Pipeline
from scrapy_puls.core.scheduler import Scheduler
from scrapy_puls.core.spider import Spider
from scrapy_puls.http_.request import Request


class Engine(object):
    def __init__(self):
        """实例化各个模块"""
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

    def start(self):
        """提供一个接口对外请求引擎的方法start"""
        self.__start()

    def __start(self):
        """提供一个私有的启动引擎的方法，用于实现核心逻辑"""

        # 调用爬虫start_request方法，获取起始请求对象
        request = self.spider.start_request()

        # 调用调度器的add_request方法，把请求添加到队列中
        self.scheduler.add_request(request)

        # 调用调度器get_request方法，取出请求对象
        request = self.scheduler.get_request()

        # 调用下载器get_response 方法，获得响应对象
        response = self.downloader.get_response(request)

        # 调用爬虫， 传入response，解析数据
        result = self.spider.parse(response)

        # 区分result是item 还是request请求对象(url)
        if isinstance(result, Request):
            # 如果是请求对象 把这个请求放进调度器队列
            self.scheduler.add_request(result)
        else:
            # 如果解析结果是数据，调用pipeline
            # process_item 处理数据
            self.pipeline.process_item(result, self.spider)












