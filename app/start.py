#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

import time,os


login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
app = Flask(__name__)


bootstrap = Bootstrap(app)
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root密码:@106.14.195.238:3306/数据库名称?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
app.config['SECRET_KEY']='chaogenizhenshuai'
db=SQLAlchemy(app)