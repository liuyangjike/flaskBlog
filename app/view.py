#!/usr/bin/env python
# -*- coding:utf-8 -*-

from artical_view import *
from user_view import *



@app.route('/about')
def about():
    return render_template('about.html',name=session.get('name'))


@app.route('/git')
def git():
    return redirect('https://github.com/captainChaozi/flaskBlog')



@app.route('/admin/')
def admin():
    return render_template('admin.html',name=session.get('name'))




@app.route('/quit')
def quit():
    session['name']=None
    return redirect(url_for('index'))





# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))


# @app.route('/secret')
# @login_required


@app.errorhandler(404)
def not_find(error):
    return render_template('error.html'), 404
@app.route('/')
def index():
    articals = Artical.query.order_by(db.desc(Artical.artical_time))
    return render_template('index.html', articals=articals, Artical_class=Artical_class,name=session.get('name'))