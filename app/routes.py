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
