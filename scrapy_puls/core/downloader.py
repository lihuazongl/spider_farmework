import requests

from ..http_.response import Response
# 下载器模块 用于发送请求，获取响应数据

class Downloader(object):

    def get_response(self, request):
        # 根据请求获取响应数据
        # 使用request模块来发送请求
        if request.method.upper() == 'GET':
            # 如果是GET请求使用get
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers, data=request.data)
        else:
            raise Exception('暂时不支持除POST和GET以外的请求')

        # 将resp对象封装 返回
        return Response(resp.url, status_code=resp.status_code, body=resp.content)