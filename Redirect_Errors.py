# Redirects and Errors
# Flask class has a redirect() function. When called, it returns a response object and redirects user to another target location with specified status code.
# Prototype of redirect() function: Flask.redirect(location, statuscode, response)
# -- Location parameter is the URL where response shuld be redirected.
# -- Status code sent to browser's header, defaults to 302
# -- Response parameter is is used to instantiate response.  
# Standardized Status Code:
    # HTTP_300_MULTIPLE_CHOICES
    # HTTP_301_MOVED_PERMANTENTLY
    # HTTP_302_FOUND(default)
    # HTTP_303_SEE_OTHER
    # HTTP_304_NOT_MODIFIED
    # HTTP_305_USE_PROXY
    # HTTP_306_RESERVED
    # HTTP_307_TEMPORARY_REDIRECT
# Flask class has abort() function to early exit, with an error code.
# Syntax: Flask.abort(code)
# Code Parameters takes one of the following values:
    # 400 -- Bad Request
    # 401 −- for Unauthenticated
    # 403 −- for Forbidden
    # 404 −- for Not Found
    # 406 −- for Not Acceptable
    # 415 −- for Unsupported Media Type
    # 429 −- Too Many Requests
    
from flask import Flask, redirect, url_for, render_template, request, abort
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug = True)    
    