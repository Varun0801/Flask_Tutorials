# HTML form with its enctype attribute set to 'multipart/form-data' and method attribute set to POST.
# The URL handler fetches file from request.files[] object and saves it to the desired location.
# Each uploaded file is first save in a temporary location on the server, before it is actually saved to its ultimatr location.
# Name of destination fil can be hand-coded or can be obtained from filename property of request.files[file] object.
# However, recommended way is to obtain a secure version of it using secure_filename() function.  
# Syntax: from werkzeug import secure_filename
# define path of default upload folder and maximum size of uploaded file in configuration setting in Flask object.
# app.config['UPLOAD_FOLDER'] --> Defines path for upload folder
# app.config['MAX_CONTENT_PATH'] --> Specifies maximum size of file to be uploaded - in bytes.

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug = True)
    
# Run it on http://localhost:5000/uploader