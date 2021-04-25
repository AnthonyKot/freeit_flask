from app import app
from flask import render_template

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/html')
def html():
    user = {'username': 'Медвед'}
    return '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Привет, ''' + user['username'] + '''!</h1>
            </body>
        </html>'''

@app.route('/template')
def template():
    user = {'username': 'bear'}
    return render_template('template.html', title='Home', user=user)

@app.route('/if1')
def if1():
    user = {'username': 'the user'}
    return render_template('if.html', user=user)

@app.route('/if2')
def if2():
    return render_template('if.html', user=None)

@app.route('/for')
def for_route():
    user = {'username': 'FreeIt user'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('for.html', title='Home', user=user, posts=posts)
