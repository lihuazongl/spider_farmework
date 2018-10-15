# 管道模块
# 处理以爬取的数据

class Pipeline(object):

    def process_item(self, item, spider):
        """处理item数据"""
        print(item.data)

        return item
