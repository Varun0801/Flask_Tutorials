# Unlike a Cookie, Session data is stored on server.
# Session is a time interval between client logs into a server and it log out of it.
# Data which is needed to be held across this session, is stored in a temporary directory on server.
# Session with each client is assigned a Session ID.
# Session data is stored on top of cookies and server signs them crypographically.
# For this encryption, Flask application needs a SECRET_KEY defined.
# Session object is also a directory object containing key-value pairs of session variables and associated values.
# To set secret key -- app.secret_key = 'XUHFF245@&(*(#Jfydslkjh<>>{+_$%'
# To set a session variable -- session(varibale) = value
# To release a session variable -- session.pop(variable, None)
# Flask will take the values you put into the session object and serialize them into a cookie.

from flask import Flask, session, redirect, url_for, render_template, request
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <b><a href = '/login'></b>" + \
           "click here to log in</b></a>"

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    #remove the username from the session if it is there
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)

        