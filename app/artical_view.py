#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from start import *
from flask import redirect, render_template, request, jsonify, session, url_for
from dbmodel import *


@app.route('/add_artical', methods=['POST'])
def add_artical():
    artical_content = request.form.get('content')
    artical_title = request.form.get('artical_title')
    artical_summary = request.form.get('artical_summary')
    artical_class = request.form.get('artical_class')
    artical_time = datetime.now()
    artical = Artical(artical_title, artical_content, artical_time, artical_summary, artical_class, )
    db.session.add(artical)
    db.session.commit()
    return render_template('artical.html', thehtml=artical_content, artical_title=artical_title,
                           name=session.get('name'))


@app.route('/articallist/<int:artical_class_id>')
def artical_list(artical_class_id):
    articals = Artical.query.filter(Artical.acid == artical_class_id).all()
    articals_class = Artical_class.query.filter(Artical_class.ac_id == artical_class_id).all()
    return render_template('articallist.html', articals=articals, articals_class=articals_class,
                           name=session.get('name'))


@app.route('/artical/<int:artical_id>')
def get_artical(artical_id):
    a_artical = Artical.query.filter(Artical.artical_id == artical_id).all()[0]
    comments = Comment.query.filter(Comment.artid == artical_id).all()

    return render_template('getartical.html', comments=comments,
                           a_artical=a_artical, name=session.get('name'))


@app.route('/savecomment', methods=['POST'])
def save_comment():
    artname = request.form.get('artical_title')
    a_artical = Artical.query.filter(Artical.artical_name == artname).all()[0]
    artid = Artical.query.filter(Artical.artical_name == artname).all()[0].artical_id
    artical_content = Artical.query.filter(Artical.artical_name == artname).all()[0].artical_content
    user_comment = request.form.get("text_area")
    user_name=request.form.get('user_name')
    user_id=Users.query.filter(Users.user_name==user_name).first().user_id
    comment = Comment(user_comment, artid, user_id)
    db.session.add(comment)
    db.session.commit()
    comments = Comment.query.filter(Comment.artid == artid).all()
    return render_template('commitlist.html', comments=comments, artical_content=artical_content,a_artical=a_artical,
                           name=session.get('name'))


@app.route('/comment', methods=['POST'])
def comment():
    user_comment = request.form.get("content")
    d = {'comment': user_comment}
    return jsonify(d)

# @app.route('/get_user_comments', methods=['POST'])
# def get_user_comments():
#     user_name = request.form.get('name')
#     user_id = Users.query.filter(Users.user_name == user_name).user_id
#     comments = Comment.query.filter(Comment.user_id == user_id).all()
#
#     return jsonify(comments)
