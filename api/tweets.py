# -*- coding: latin1 -*-

from flask import request

@app.route('/login')
def tweets():
    username = request.args.get('username')
    password = request.args.get('password')
