class Response(object):
    def __init__(self, url, status, params, headers, body):

        self.url = url
        self.status = status # 状态码
        self.headers = headers # 响应头
        self.body = body # 响应体数据,二进制
