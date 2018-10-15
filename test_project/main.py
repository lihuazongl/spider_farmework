# 用于爬虫框架的测试

from scrapy_puls.core.engine import Engine



def main():
    # 创建引擎对象
    engine = Engine()
    # 启动引擎
    engine.start()


if __name__ == '__main__':
    main()