class Response(object):
    def __init__(self, url, status_code=200, headers={}, body=None):

        self.url = url
        self.status_code = status_code # 状态码
        self.headers = headers # 响应头
        self.body = body # 响应体数据,二进制
