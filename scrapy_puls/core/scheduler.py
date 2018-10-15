# 调度器

# six: 第三方模块， 专门处理Python2 和 python3 的兼容
from six.moves.queue import Queue


class Scheduler(object):
    """
    功能
    1 缓存请求
    2 请求去重
    """
    def __init__(self):
        # 创建队列， 用于缓存请求
        self.queue = Queue()

    def add_request(self, request):
        """把请求对象添加到队列"""
        self.queue.put(request)

    def get_request(self):
        """将请求取出"""
        self.queue.get()

    def filter_requests(self, request):
        """实现请求去重，如果该请求需要过滤就返回True，不需要过滤返回False"""
        # TODU 待实现
        pass







