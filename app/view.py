#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from start import *
from flask import redirect, render_template, request, jsonify
from dbmodel import *

@app.route('/111')
def hello_flask():
    # return render_template('about.html')
    return 'hello flask'




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


@app.route('/')
def index():
    articals = Artical.query.order_by(db.desc(Artical.artical_time))
    return render_template('index.html',articals=articals,Artical_class=Artical_class)



@app.route('/add_artical', methods=['POST'])
def add_artical():
    artical_content = request.form.get('content')
    artical_title=request.form.get('artical_title')
    artical_summary=request.form.get('artical_summary')
    artical_class=request.form.get('artical_class')
    artical_time=datetime.now()
    artical=Artical(artical_title,artical_content,artical_time,artical_summary,artical_class,)
    db.session.add(artical)
    db.session.commit()
    return render_template('artical.html', thehtml=artical_content,artical_title=artical_title)


@app.route('/articallist/<int:artical_class_id>')
def artical_list(artical_class_id):
    articals=Artical.query.filter(Artical.acid==artical_class_id).all()
    articals_class=Artical_class.query.filter(Artical_class.ac_id==artical_class_id).all()
    return render_template('articallist.html',articals=articals ,articals_class=articals_class)

@app.route('/artical/<int:artical_id>')
def get_artical(artical_id):
    a_artical=Artical.query.filter(Artical.artical_id==artical_id).all()[0]
    return render_template('getartical.html',a_artical=a_artical,)



@app.route('/savecomment',methods=['POST'])
def save_comment():
    artname=request.form.get('artical_title')
    artid=Artical.query.filter(Artical.artical_name==artname).all()[0].artical_id
    artical_content=Artical.query.filter(Artical.artical_name==artname).all()[0].artical_content
    user_comment = request.form.get("text_area")
    comment=Comment(user_comment,artid,1)
    db.session.add(comment)
    db.session.commit()
    comments=Comment.query.filter(Comment.artid==artid).all()
    return render_template('commitlist.html', comments=comments,artical_content=artical_content)






@app.route('/comment', methods=['POST'])
def comment():
    user_comment = request.form.get("content")
    d = {'comment': user_comment}
    return jsonify(d)


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



