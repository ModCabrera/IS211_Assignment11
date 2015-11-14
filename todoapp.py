#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To Do List Flask Application"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

email_adresses = [] #email output
tasks = []
priorities = []

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods= ['POST'])
def submit():
    task = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    email_adresses.append(email)
    tasks.append(task)
    priorities.append(priority)
    return render_template('index.html',
                           email_adresses=email_adresses,
                           tasks=tasks,
                           priorities=priorities)


if __name__ == '__main__':
    app.run(debug=True)
