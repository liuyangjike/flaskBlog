#!/usr/bin/env python
# -*- coding:utf-8 -*-
from start import db


# from sqlalchemy import  Column,Integer,Text,String,ForeignKey
# from sqlalchemy.orm import relationship



class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.role_id))
    articals = db.relationship('Artical', backref='role')
    comments = db.relationship('Comment', backref='role')

    def __init__(self, user_name, password, user_email):
        self.name = user_name
        self.password = password
        self.user_email = user_email


class Artical_class(db.Model):
    __tablename__ = 'artical_class'
    ac_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ac_class = db.Column(db.String(64), nullable=False)
    articals = db.relationship('Artical', backref='role')

    def __init__(self, ac_id, ac_class):
        self.ac_id = ac_id
        self.ac_class = ac_class

class Artical(db.Model):
    __tablename__ = 'articals'
    artical_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artical_name = db.Column(db.String(64), nullable=False)
    artical_time = db.Column(db.DateTime, nullable=False)
    artical_content = db.Column(db.Text, nullable=False)
    acid = db.Column(db.Integer, db.ForeignKey(Artical_class.ac_id))
    userid = db.Column(db.Integer, db.ForeignKey(Users.user_id))
    comments = db.relationship('Comment', backref='role')

    def __init__(self,artical_id,artical_name,artical_content,artical_time):
        self.artical_id = artical_id
        self.artical_name = artical_name
        self.artical_content = artical_content
        self.artical_time = artical_time




class Comment(db.Model):
    __tablename__='comments'
    comment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    comment_content=db.Column(db.Text,nullable=False)
    artid=db.Column(db.Integer,db.ForeignKey(Artical.artical_id))
    user_id=db.Column(db.Integer,db.ForeignKey(Users.user_id))
    def __init__(self,comment_id,comment_content):
        self.comment_id=comment_id
        self.comment_content=comment_content



