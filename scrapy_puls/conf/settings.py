
# 注意 先要把默认配置导入, 再导入用户配置
# 因为后导入用户配置 ,才会覆盖默认配置, 用户的配置才会生效

# 把所有默认配置导入到当前配置文件中
from .default_settings import *

# 导入用户项目中的配置文件settings.py
# 报红是因为pycharm没有识别到用户路径
# 执行程序的时候会自动识别
from settings import *


# 查看程序加载文件顺序
# import sys
# for path in sys.path:
#     print(path)
"""
文件加载路径 顺序

/home/python/.virtualenvs/pachong/bin/python /home/python/Desktop/spider_framework/test_project/main.py
/home/python/Desktop/spider_framework/test_project
/home/python/Desktop/spider_framework
/home/python/.virtualenvs/pachong/lib/python35.zip
/home/python/.virtualenvs/pachong/lib/python3.5
/home/python/.virtualenvs/pachong/lib/python3.5/plat-x86_64-linux-gnu
/home/python/.virtualenvs/pachong/lib/python3.5/lib-dynload
/usr/lib/python3.5
/usr/lib/python3.5/plat-x86_64-linux-gnu
/home/python/.virtualenvs/pachong/local/lib/python3.5/site-packages
/home/python/.virtualenvs/pachong/local/lib/python3.5/site-packages/scrapy_plus-1.0-py3.5.egg
/home/python/.virtualenvs/pachong/lib/python3.5/site-packages
/home/python/.virtualenvs/pachong/lib/python3.5/site-packages/scrapy_plus-1.0-py3.5.egg
/snap/pycharm-professional/89/helpers/pycharm_matplotlib_backend"""