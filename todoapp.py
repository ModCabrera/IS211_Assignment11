#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To Do List Flask Application"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks = []

class Task:
    email = None
    task = None
    priority = None

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods= ['POST'])
def submit():
    desc = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    task = Task()
    task.task = desc
    task.priority = priority
    task.email = email
    tasks.append(task)
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)




"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''To Do List Flask Application'''

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

emails= [] #email output
tasks = []
priorities = []

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    emails.append(email)
    tasks.append(task)
    priorities.append(priority)
    data = zip(tasks, priorities, emails)
    return render_template('index.html', data=data)

@app.route('/clear')
def clear():
    email_adresses = []
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



index.html



<!DOCTYPE html>
<html>
  <head>
    <title>To Do App!</title>
    <h1><img src='http://localhost:5000/static/todo_logo.jpg'></h1>
    <h2>Your To Do List:</h2>
  </head>
  
      <style = type='text/css'>
      body
      {
        font-size:16px;
        margin-top:10;
        font-family:Arial, sans-serif;
        text-decoration:none;
        padding:10px 0;
      }

      form
      {
        font-size:16px;
        margin-top:20;
        font-family:Arial, sans-serif;
        text-decoration:none;
        padding:15px 0;
      }
      
      table
      {
        font-size:16px;
        margin-top:20;
        font-family:Arial, sans-serif;
        text-decoration:none;
        padding:20px 0;
      }  
      </style>
  <body>
    <form action="/submit" method="post">
      Task : <br>
      <input type="text" name="task">
      <br>
      E-Mail : <br>
      <input type="text" name="email">
      <select name="priority">
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
      <input type="submit" value="Add To Do Item">
      </select>
    </form>
    
    <table border="1" style="width:50%">
      <tr>
        {% for task in data[0] -%}
        <td>{{ task }}</td
        {% endfor %}
      </tr>       
    </table>
    <form>
        <form action="/clear">
        <input type="submit" value="Clear">
    </form>
  </body>
</html>


"""
