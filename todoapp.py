#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To Do List Flask Application"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks = []
emails = []
priorities = []

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods= ['POST'])
def submit():
    task = request.form['task']
    tasks.append(task)
    priority = request.form['priority']
    priorities.append(priority)
    email = request.form['email']
    emails.append(email)
    return redirect('/')


if __name__ == '__main__':
    app.run()
