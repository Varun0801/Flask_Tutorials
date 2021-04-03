# A good GUI based application provides feedback to user about the interaction.
# Desktop applications use dialog or message box.
# JavaScript uses alert for similar purposes.
# Flashing system of Flask Framework makes it possible to craete a message in one view and render it in a view function called next.
# Flask.flash() method passes a message to next request which generally is a template.
# flask(message, category)
# message parameter is the actual message to be flashed.
# category parameter is optional. It can either 'error', 'info' or 'warning'.
# In order to remove message from session, template calls get_flashed_messages(with_categories, category_filter)
# Fisrt parameter is a tuple if received messages are having category.
# Second parameter is useful to display only specific messages.


from flask import Flask, redirect, url_for, render_template, request, flash
# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'random_string'

@app.route('/')
def index():
    return render_template('Index1.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            flash('log out before you login again')
            return redirect(url_for('index'))
        
    return render_template('login.html', error = error)

if __name__ == '__main__':
    app.run(debug = True) 