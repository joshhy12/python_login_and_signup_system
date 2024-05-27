from flask import Flask, render_template, redirect, request, session
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)

app.secret_key = "your_secret_key"




from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])







@app.route('/')
def index():
    return redirect('/signup')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle form submission for login
        email = form.email.data
        password = form.password.data
        # Verify the user credentials from the database or file
        # Set a session variable to track the logged-in user
        session['username'] = email
        return redirect('/home')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Handle form submission for sign-up
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # Store the user details in a database or file
        # Redirect the user to the home page and set the session variable
        session['username'] = username
        return redirect('/home')
    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    username = session.get('username')
    if not username:
        return redirect('/login')
    return render_template('home.html', username=username)


if __name__ == '__main__':
    app.run()
