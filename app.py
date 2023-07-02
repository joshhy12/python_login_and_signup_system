from flask import Flask, render_template, redirect, request, session


app = Flask(__name__, static_folder='static')

app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return redirect('/signup')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle form submission for sign-up
        username = request.form['username']
        password = request.form['password']
        # Store the user details in a database or file
        # Redirect the user to the home page and set the session variable
        session['username'] = username
        return redirect('/home')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission for login
        username = request.form['username']
        password = request.form['password']
        # Verify the user credentials from the database or file
        # Set a session variable to track the logged-in user
        session['username'] = username
        return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    username = session.get('username')
    if not username:
        return redirect('/signup')
    return render_template('home.html', username=username)

if __name__ == '__main__':
    app.run()
