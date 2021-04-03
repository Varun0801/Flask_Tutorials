# A cookie is stored on client's computer as a text file. Its purpose is to remember and track data pertaining to client's usage for better visitor experience and site statistics.
# Request object contains a cookie attribute. It is a dictionary object of all cookie variables and corresponding values that client has transmitted. Cookie also stores its expiry time, path and domain name of site.
# In Flask, cookies are set on response object.
# Use make_response() function to get the response object from return value of a view function.
# Use set_cookie() function of response object to store a cookie.
# get() method of request.cookies attribute is used to read a cookie.

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)   
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+ str(name) +'</h1>'

if __name__ == '__main__':
    app.run(debug = True)
