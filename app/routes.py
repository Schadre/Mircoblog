from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Saint'}
    posts = [
        {
            'author': {'username': 'Hannibal'},
            'body': 'Killing it out here in LA!'
        },
        {
            'author': {'username': 'Clarice'},
            'body' : 'I am going to find this guy!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)