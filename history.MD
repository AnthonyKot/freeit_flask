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


## 3
# to add some Jinja to the project
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


## 4 Jinja flow control directives
# let's add if.html template
<html>
    <body>
        <h1>
          {% if user.username %}
            Hello {{ user.username }}
          {% else %}
            Welcome to FreeIT server
          {% endif %}
        </h1>
    </body>
</html>
# and 2 test routes
@app.route('/if1')
def if1():
    user = {'username': 'the user'}
    return render_template('if.html', user=user)

@app.route('/if2')
def if2():
    return render_template('if.html', user=None)

## note: if you don't provide user object flask would fail

# check: open http://localhost:5000/if1
# check: open http://localhost:5000/if2

# it's also possible to use {% for ... %} directive
# let's add for.html template
<html>
    <head>
        {% if title %}
        <title>{{ title }} - FreeIT</title>
        {% else %}
        <title>Welcome to FreeIT</title>
        {% endif %}
    </head>
    <body>
        <h1>Hi, {{ user.username }}!</h1>
        {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
        {% endfor %}
    </body>
</html>
# and for route
app.route('/for')
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
# check: open http://localhost:5000/for


## 5
# Jinja supports composition of templates
# let's add app/templates/base.html template share common details
<html>
    <head>
      {% if title %}
      <title>{{ title }} - FreeIT</title>
      {% else %}
      <title>Welcome to FreeIT</title>
      {% endif %}
    </head>
    <body>
        <div>FreeIT: <a href="/">Home</a></div>
        <hr>
        {% block content %}{% endblock %}
    </body>
</html>
# then child.html may reuse base.html to display title and navigation
{% extends "base.html" %}

{% block content %}
    <h1>Hi, {{ user.username }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}
# and use new route
@app.route('/child')
def children():
    user = {'username': 'FreeIt user'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('child.html', title='Children', user=user, posts=posts)

## BONUS
ssh -R 80:localhost:5000 nokey@localhost.run
# ssh is needed


##  LESSON_12
export FLASK_APP=freeit.py
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate

flask db init

Creating directory /Users/rdyto1/Projects/freeit_flask/migrations ... done
Creating directory /Users/rdyto1/Projects/freeit_flask/migrations/versions ... done
Generating /Users/rdyto1/Projects/freeit_flask/migrations/alembic.ini ... done
Generating /Users/rdyto1/Projects/freeit_flask/migrations/env.py ... done
Generating /Users/rdyto1/Projects/freeit_flask/migrations/README ... done
Generating /Users/rdyto1/Projects/freeit_flask/migrations/script.py.mako ... done
Please edit configuration/connection/logging settings in
'/Users/rdyto1/Projects/freeit_flask/migrations/alembic.ini' before proceeding.

## migrate => upgrade

flask db migrate -m "users table"

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
Generating /Users/rdyto1/Projects/freeit_flask/migrations/versions/e517276bb1c2_users_table.py ... done

flask db upgrade

## terminal

>>> from app import db
>>> from app.models import User, Post

# as an option
>>> flask shell

>>> u = User(username='anton', email='anton@example.com')
>>> db.session.add(u)
>>> db.session.commit()

>>> users = User.query.all()
>>> users

>>> p = Post(body='Anton was here', author=u)

>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)

>>> User.query.order_by(User.username.desc()).all()



## LOGIN

pip install flask-login
pip install Flask-OpenID
pip install email_validator

# NB: don't forget UserMixin


# LESSON_13

# add Profile Page

@app.route('/user/<nickname>')
@login_required

| <a href="{{ url_for('user', username = current_user.username) }}">Your Profile</a>
| <a href="{{ url_for('logout') }}">Logout</a>

posts = Post.query.join(User).filter_by(username = username)

# make user a pretty thing

from hashlib import md5
# ...
class User(db.Model):
    # ...
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

<table>
    <tr valign="top">
        <td><img src="{{user.avatar(128)}}"></td>
        <td><h1>User: {{user.nickname}}</h1></td>
    </tr>
</table>

{% include 'post.html' %}

#commit

role = db.Column(db.SmallInteger, default = 0)
about_me = db.Column(db.String(140))
last_seen = db.Column(db.DateTime)

# migration

flask db migrate -m "add more user data"
flask db upgrade

{% if user.about_me %}<p>{{user.about_me}}</p>{% endif %}
{% if user.last_seen %}<p><i>Last seen on: {{user.last_seen}}</i></p>{% endif %}

@app.before_request for last_seen

# expalain utcnow
