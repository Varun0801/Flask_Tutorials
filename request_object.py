# Request Object in Flask
# Data from client's web page is sent to server as a global request object.
# In order to process request data, it should be imported from flask module.
# Important attributes of request object
    # Form: A MultiDict with the parsed form data from POST or PUT requests.
    # args: A MultiDict with the parsed contents of the query string.(The Part in the URL after the question mark.)
    # values: A CombinedMultiDict with the contents of both form and args.
    # cookies: A dict with the contents of all cookies transmitted with the request.
    # headers: The incoming request headers as a dictionary like object.
    # data: Contains the incoming request data as string in case it came with a minetype Flask does not handle.
    # files: A MultiDict with files uploaded as part of a POST or PUT request. Each file is stored as FileStorage object. Behaves like a standard file object you know from Python.
    # Also has a save() function that can store the file on the filesystem.
    # environ: The underlying WSGI environment.
    # method: The current request method (POST, GET, etc.)
    # module: The name of the current module if the request was dispatched to an actual module.
    # routing_exception: None : if matching the URL failed, this is the exception that will be raised as part of the request handling. This is usually a NotFound exception or something similar.
 
# HTML form data is submitted by POST method.
# Function bound to URL receives form data in request.form dictionary object
# This form object is forwarded to template for processing.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)
    
if __name__ == '__main__':
    app.run(debug = True)
    