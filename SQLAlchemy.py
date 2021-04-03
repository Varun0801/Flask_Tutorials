# Most Programming language platforms are object oriented.
# Data in RDBMS servers on the other hand is stoted as tables.
# Object relation mapping is a technique of mapping object parameters to underlying DBMS table structure.
# An ORM API provides methods to perform CRUD operations without having to write raw SQL statements.
# SQLAlchemy Object Relational Mapper presents a method of associating Python Class with database table, and objects with rows in their corresponding tables. 
# Flask-SQLAlchemy is the Flask extension that adds support for SQLAlchemy to your Flask application.

# Step 1 − Install Flask-SQLAlchemy extension.
# pip install flask-sqlalchemy

# Step 2 − You need to import SQLAlchemy class from this module.
# from flask_sqlalchemy import SQLAlchemy

# Step 3 − Now create a Flask application object and set URI for the database to be used.
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

# Step 4 − Then create an object of SQLAlchemy class with application object as the parameter. This object contains helper functions for ORM operations.
# It also provides a parent Model class using which user defined models are declared.
# Each Model class corresponds to table in database.

# -------------------
## A students model is created:
# db = SQLAlchemy(app)
# class students(db.Model):
#    id = db.Column('student_id', db.Integer, primary_key = True)
#    name = db.Column(db.String(100))
#    city = db.Column(db.String(50))  
#    addr = db.Column(db.String(200))
#    pin = db.Column(db.String(10))

# def __init__(self, name, city, addr,pin):
#    self.name = name
#    self.city = city
#    self.addr = addr
#    self.pin = pin    
# -------------------  

# Step 5 − To create / use database mentioned in URI, run the create_all() method.
# db.create_all()

# The ORM's "handle" to the database is the Session.
# The Session object of SQLAlchemy manages all persistence operations of ORM object.
# Session object methods--
    # db.session.add(model obj) : inserts a record into mapped table.
    # db.session.delete(model obj) : deletes record from table.
    # model.query.all() : retrieves all records from table (corresponding to SELECT query)
    # model.query.filter(condition) : You can apply filter to retrived record.
            # Ex: Students.query.filter_by(city='Hyderabad').all() 

# The entry point of the application is show_all() function bound to ‘/’ URL. 
# The Record set of students table is sent as parameter to the HTML template. 
# The Server side code in the template renders the records in HTML table form.
# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students = students.query.all() )

#The above page contains a hyperlink to ‘/new’ URL mapping new() function. 
# When clicked, it opens a Student Information form. 
# The data is posted to the same URL in POST method.

# When the http method is detected as POST, the form data is added in the students table and the application returns to homepage showing the added data.
# @app.route('/new', methods = ['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash('Please enter all the fields', 'error')
#         else:
#             student = students(request.form['name'], request.form['city'],
#             request.form['addr'], request.form['pin'])
         
#             db.session.add(student)
#             db.session.commit()
         
#             flash('Record was successfully added')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')

# CODE -------------
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], 
                               request.form['city'],
                               request.form['addr'], 
                               request.form['pin'])
         
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)

