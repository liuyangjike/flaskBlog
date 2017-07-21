#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from start import *
from flask import redirect, render_template, request, jsonify, session, url_for, flash
from dbmodel import *


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter(Users.user_email == email).first()
        if user is not None and user.verify_password(password):
            user_name = user.user_name
            session['name'] = user_name
            if user_name == 'chaoge':
                return render_template('admin.html', user_name=user_name, name=session.get('name'))
            else:
                user_id = user.user_id
                comments = Comment.query.filter(Comment.user_id == user_id).all()
                return render_template('user.html', user_name=user_name, name=session.get('name'),comments=comments)
        return render_template('login.html',information=u'用户名或者密码有误，再试试吧')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/sucess_register', methods=['POST'])
def sucess_register():
    user_email = request.form.get('email')
    exit_name = Users.query.filter(Users.user_email == user_email).first()
    if exit_name:
        return render_template('register.html', information=u'此邮箱已经被注册啦,换一个试试吧')
    user_name = request.form.get('user_name')
    exit_name = Users.query.filter(Users.user_name == user_name).first()
    if exit_name:
        return render_template('register.html', information=u'此用户名已经被注册啦,换一个试试吧')
    user_password = request.form.get('password')
    user = Users()
    user.password = user_password
    user.user_name = user_name
    user.user_email = user_email
    db.session.add(user)
    db.session.commit()
    return render_template('login.html', information=u'注册成功，赶快登录吧')


@app.route('/user/<user_name>')
def user(user_name):
    if user_name == 'chaoge':
        return render_template('admin.html', user_name=user_name, name=session.get('name'))
    user_id = Users.query.filter(Users.user_name == user_name).first().user_id
    comments = Comment.query.filter(Comment.user_id == user_id).all()
    return render_template('user.html', user_name=user_name, name=session.get('name'),comments=comments)


@app.route('/change_password', methods=['POST'])
def change_password():
    email = request.form.get('email')
    old_password=request.form.get('old_password')
    new_password=request.form.get('new_password')
    user = Users.query.filter(Users.user_email == email).first()
    if user is not None and user.verify_password(old_password):
        user.password = new_password
        db.session.add(user)
        db.session.commit()
        return render_template('login.html', information=u'修改成功，赶快登录吧')
    else:
        return render_template('user.html',information=u'原密码错了，请重新修改')


# @app.route('/get_user_comments',methods=['POST'])
# def get_user_comments():
#     user_name=request.form.get('name')
#     user_id=Users.query.filter(Users.user_name==user_name).first()
#     comments=Comment.query.filter(Comment.user_id==user_id).all()
#     return render_template('user.html',user_name=user_name,comments=comments)


