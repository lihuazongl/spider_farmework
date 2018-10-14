# item 类用于封装 爬虫爬取的数据

class Item(object):

    def __init__(self, data):
        # 使用私有变量来记录数据
        self.__data = data

    @property # 让这个方法编程一个只读属性。 能保护数据
    def data(self):
        # 返回数据的封装
        return  self.__data
