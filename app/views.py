from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

#we have imported our LoginForm class, instantiated an object from it, and sent it down to the template

#`methods` argument in the route decorator tells Flask that this view function accepts GET and POST requests. Without this the view will only accept GET requests. We will want to receive the POST requests, these are the ones that will bring in the form data entered by the user.
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         #The validate_on_submit method does all the form processing work. If you call it when the form is being presented to the user (i.e. before the user got a chance to enter data on it) then it will return False, so in that case you know that you have to render the template.

        #When validate_on_submit is called as part of a form submission request, it will gather all the data, run all the validators attached to fields, and if everything is all right it will return True, indicating that the data is valid and can be processed. This is your indication that this data is safe to incorporate into the application.

        #If at least one field fails validation then the function will return False and that will cause the form to be rendered back to the user, and this will give the user a chance to correct any mistakes. We will see later how to show an error message when validation fails.

        #When validate_on_submit returns True our login view function calls two new functions, imported from Flask. The flash function is a quick way to show a message on the next page presented to the user. In this case we will use it for debugging, since we don't have all the infrastructure necessary to log in users yet, we will instead just display a message that shows the submitted data. The flash function is also extremely useful on production servers to provide feedback to the user regarding an action.
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                          title = 'Sign In',
                          form = form,
                          providers = app.config['OPENID_PROVIDERS'])