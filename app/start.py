#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

import time,os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root123456:@localhost:3306/myblog?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
db=SQLAlchemy(app)