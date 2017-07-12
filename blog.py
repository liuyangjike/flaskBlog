#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app.view import *
from app.dbmodel import *

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)