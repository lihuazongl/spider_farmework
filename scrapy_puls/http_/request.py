class Request(object):
    def __init__(self, url, method, params, headers, data):

        self.url = url
        self.method = method
        self.headers = headers
        self.params = params # GET请求参数
        self.data = data # POST请求参数,
