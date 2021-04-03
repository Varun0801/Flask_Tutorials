from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello %s!' % name

if __name__ == "__main__":
    app.run(debug=True) 
    
# run it on http://127.0.0.1:5000/hello/Varun(or any other name)  