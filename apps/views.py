# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

from flask import request, render_template, flash, url_for, redirect, g, session, jsonify
from werkzeug.security import generate_password_hash

from apps import app, pi
from apps.models import User
from core import utils
from decorators import login_required, admin_required

import logging


@app.before_request
def load_user():
    if session.get('logged_in'):
        user = session.get('user', None)
    else:
        user = 'Guest'  # Make it better, use an anonymous User instead

    g.user = user
    g.is_superuser = True if session.get('is_superuser') else False


def join():
    if request.method == 'GET':
        return render_template('join.html')

    if request.method == 'POST':
        user_exist = None

        user_exist = User.query(User.username == request.form['username']).get()
        print user_exist

        user = User(
            username=request.form['username'], password=generate_password_hash(request.form['password']), email=request.form['email']
        )
        exist = False

        if not user_exist:
            user_create_result = user.put()
            logging.info(user_create_result)

            flash(u'회원가입을 하였습니다.', 'success')
            return redirect(url_for('home'))
        else:
            flash(u'중복되는 아이디가 존재합니다.', 'danger')
            return redirect(url_for('join'))


def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        user = User.query(User.username == request.form['username']).get()
        if user:
            if user.check_password(request.form['password']):
                session['logged_in'] = True
                if user.is_superuser:
                    session['is_superuser'] = True

                session['user'] = request.form['username']
                flash(u'로그인 하였습니다.', 'success')
                return redirect(url_for('home'))
            else:
                flash(u'잘못된 비밀번호 입니다.', 'danger')
                return redirect(url_for('home'))
        else:
            flash(u'사용자가 존재하지 않습니다.', 'danger')
            return redirect(url_for('home'))


def logout():
    session['logged_in'] = False
    g.user = 'Guest'

    flash(u'로그아웃 하였습니다.', 'success')

    return redirect(url_for('home'))


@login_required
def home():
    return render_template('home.html')


@login_required
def send_message():
    if request.method == 'POST':
        pi['test_channel'].trigger('my-event', {'message': 'hello world'})

        return jsonify(message=u"message")