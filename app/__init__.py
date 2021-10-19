# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: __init__.py.py
@time: 2017/7/13 16:38
"""
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from  flask import  Flask
from  flask_sqlalchemy import  SQLAlchemy
# from flask_bootstrap import  Bootstrap
from flask_login import LoginManager
from config import lod
from apscheduler.schedulers.background import BackgroundScheduler
from config import jobstores, executors
from flask_admin import  Admin
# from flask_moment import  Moment
app=Flask(__name__)
conf=lod()
loginManager = LoginManager(app)
app.config.from_object(conf)
# bootstrap=Bootstrap(app)
loginManager.session_protection = "strong"
loginManager.login_view='home.login'
loginManager.login_message=u'FXTest测试平台必须登录，请登录您的FXTest平台账号！'
db=SQLAlchemy(app)
# jobstores = {
#     'sqlalchemy': SQLAlchemyJobStore(engine=db),
# }
# moment=Moment(app)
sched = BackgroundScheduler(jobstores=jobstores, executors=executors)
admin=Admin(app,name=u'FXTest系统管理后台')
from  app import  views ,models,url,apiadmin