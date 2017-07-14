#!/usr/bin/env python
# -*- coding:utf-8 -*-
from start import db


# from sqlalchemy import  Column,Integer,Text,String,ForeignKey
# from sqlalchemy.orm import relationship



class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(64), unique=True)
    users = db.relationship('Users', backref='role')

    def __init__(self,  role_name):
        self.role_name = role_name


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.role_id))
    comments = db.relationship('Comment', backref='user')

    def __init__(self, user_name, password, user_email):
        self.name = user_name
        self.password = password
        self.user_email = user_email


class Artical_class(db.Model):
    __tablename__ = 'artical_class'
    ac_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ac_class = db.Column(db.String(64), nullable=False)
    articals = db.relationship('Artical', backref='artical_class')

    def __init__(self, ac_class):
        self.ac_class = ac_class


class Artical(db.Model):
    __tablename__ = 'articals'
    artical_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artical_name = db.Column(db.String(64), nullable=False)
    artical_summary = db.Column(db.Text, nullable=False)
    artical_time = db.Column(db.DateTime, nullable=False)
    artical_content = db.Column(db.Text, nullable=False)
    acid = db.Column(db.Integer, db.ForeignKey(Artical_class.ac_id))
    artical_comment = db.relationship('Comment', backref='artical')

    def __init__(self, artical_name, artical_content, artical_time, artical_summary,acid):
        self.artical_name = artical_name
        self.artical_content = artical_content
        self.artical_time = artical_time
        self.artical_summary = artical_summary
        self.acid=acid



class Comment(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment_content = db.Column(db.Text, nullable=False)
    artid = db.Column(db.Integer, db.ForeignKey(Artical.artical_id))
    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))

    def __init__(self,  comment_content,artid,user_id):
        self.comment_content = comment_content
        self.artid=artid
        self.user_id=user_id




def creatdb():
    db.drop_all()
    db.create_all()

    u1=Users('chaozi','passworld','1095087479@qq.com')
    db.session.add(u1)
    db.session.commit()

    u2 = Users('chaoge', '123456', '18301951396@qq.com')
    db.session.add(u2)
    db.session.commit()

    ac1=Artical_class(u'python')
    db.session.add(ac1)
    db.session.commit()

    ac2=Artical_class(u'web框架')
    db.session.add(ac2)
    db.session.commit()

    ac3=Artical_class(u'前端')
    db.session.add(ac3)
    db.session.commit()

    ac4=Artical_class(u'编程')
    db.session.add(ac4)
    db.session.commit()

    ac5=Artical_class(u'我执')
    db.session.add(ac5)
    db.session.commit()

    admin=Role('admin')
    db.session.add(admin)
    db.session.commit()

    g_user=Role('g_user')
    db.session.add(g_user)
    db.session.commit()

if __name__=='__main__':
    creatdb()


