# 爬虫中间件 预处理处理爬虫 请求对象和响应对象


class SpiderMiddleware(object):

    def process_request(self, request):
        print('SpiderMiddleware-process_request-{}'.format(request.url))

        return request

    def process_response(self, response):
        print('SpiderMiddleware-process_response-{}'.format(response.url))

        return response
