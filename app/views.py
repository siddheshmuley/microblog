from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Siddhesh'}#dummy user
    posts = [#dummy posts
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Gainesville!'
        },
        {
            'author':{'nickname':'Lara'},
            'body':'Infinity war is gonna be awesome!'
        }
    ]
    return render_template('index.html',
                          title='Home',
                          user=user,
                          posts=posts)