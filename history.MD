## 1
# configure ENV
python3 -m venv freeit_flask
source freeit_flask/bin/activate
pip install flask
# check: python >> import flask

## as an option add freeit_flask and **.pyc to .gitignore

## 2
# create "Hello world" Flask app
mkdir app && cd app
# files needed
freeit_flask/
  freeit_flask/
  app/
    __init__.py => module definition
    routes.py => application routes
  freeit.py => main script
# export PATH VAR
export FLASK_APP=freeit.py
flask run
# check: open http://localhost:5000/

## as an option """flask run &""" runs in backgound
## but then to stop if get PID from """ps -ef""" and run """sudo kill -9 <FLASK_PID>"""

## 3 add some Jinja
# add html method to route /html path
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
# check: open http://localhost:5000/html

# add Jinja2 template
mkdir app/templates
echo '<html>
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>' > app/templates/template.html
# change routes to render_template
@app.route('/template')
def template():
    user = {'username': 'bear'}
    return render_template('template.html', title='Home', user=user)
# check: open http://localhost:5000/template
