# url_for() function is very useful for dynamically building URL for a specific function.
# The Function accepts name of function as first argument, and one or more keywords arguments,
#     each corresponding to varibale part of URL.
# It allows you to change URLs in one go, without having to remember to change URLs all over   #     the place.
# URL building will handle escaping of special characters and Unicode data transparently for  #     you, so you don't have to deal with them.
# If your application is places outside the URL, url_for() will handle that properly for you.

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == "__main__":
    app.run(debug=True) 