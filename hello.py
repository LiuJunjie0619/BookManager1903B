# -*- encoding: utf-8 -*-
# 导包
from flask import Flask
from day01.config import *


# 实例化APP
app = Flask(__name__)
# app.config['DEBUG'] = True
# 1、加载配置类
# app.config.from_object(ProjectConfig)

# 2、从文件加载配置
# app.config.from_pyfile('config.txt')

#3、从环境变量加载
app.config.from_envvar('config01')


# 配置加载
# 1、通过配置对象加载（最常用的方式）


# 路由地址，网址，URL
# 视图函数
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    # debug = True 开启调试模式
    app.run()
    # app.run()
