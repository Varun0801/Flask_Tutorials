# HTTP is structured text that uses logical links between nodes containing text.
# HTTP is the protocolto exchange or tranfer hypertext.
# HTTP defines methods to indicate the desired actions to be performed on the identified resource.
# Resource corresponds to a file or the Output of an executable residing on the server.
# HTTP/1.0 specification defined the GET, POST, and the HEAD methods.
# HTTP/1.1 specification added 5 new methods: OPTIONS, PUT, DELETE, TRACE, and CONNECT.

## GET : Sends Data in unencrypted form to the server. Most Commom Method
## HEAD : Same as GET, but without response body.
## POST : Used to send HTML form data to server. Data received by POST method is not cached by server.
## PUT : Replaces all current represenations of the target resource with the uploaded content.
## DELETE : Removes all current representations of the target resource gien by a URL.
## TRACE : Echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers.
## CONNECT : Coverts the request connection to a transparent TCP/IP tunnel to facilitate SSL-encrypted communcation.

# By Default Flask route responds to GET requests. However this preference can be altered by providing methods argument to route() decorator.

#from flask import Flask, request
#app = Flask(__name__)
#@app.route('function',methods = ['POST','GET'])
#def function():
#    if request.method == 'POST':
        #statement1
        #statement2
        #...
#    else:
        #statement1
        #statement2
        #...
        
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return 'welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome',name=user))
    
if __name__ == '__main__':
    app.run(debug = True)