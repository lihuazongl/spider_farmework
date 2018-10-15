
import logging


# 设置日志等级
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)


# 设置对应的日志等级输出的内容
logging.debug('调试模式')

logging.info('普通模式:输出程序运行一些状态信息')

logging.warning('警告信息;不建议使用')

logging.error('错误信息')

logging.critical('严重错误')

try:
    raise Exception('抛出错误')
except Exception as ex:
    # 捕获错误信息到日志
    logging.exception(ex)