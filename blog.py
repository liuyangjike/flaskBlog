#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, redirect, render_template,request
from flask.ext.bootstrap import Bootstrap
import time,os

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/articleList')
def articleList():
    return u'文章列表'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/git')
def git():
    return redirect('https://github.com/captainChaozi/flaskBlog')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/user/')
def user():
    return render_template('user.html')


@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/addart',methods=['POST'])
def add_artical():
    thehtml=request.form.get('content').encode('utf-8')
    return  thehtml
# @app.route('/uploadimage',methods=['POST'])
# def up_load_image():
#     if request.method=='POST':
#         file = request.files['file']
#         name = file.filename
#         extentions = name.split('.')[1]
#         firstname = time.strftime('%Y%m%d%H%M%S')
#         name = firstname + '.' + extentions
#         strurl = os.path.join(app.config['UPLOAD_FOLDER'], name)
#         file.save(strurl)
#         baseurl = request.base_url.split('upload')[0]
#         adress = baseurl + 'uploads/' + name
#         return render_template('upload.html')
#     return render_template('upload.html')

@app.errorhandler(404)
def not_find(error):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'upload/artical'
    app.run(debug=True)
