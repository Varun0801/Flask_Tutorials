# HTML provides a <form> tag which is used to design a user interface.
# Form elements such as text, +input, radio, select etc.
# Data entered by a user is submitted in the form of Http request message to the server side script by either GET or POST method.
# The Server side script has to recreate the form elements from http request data. So in effect, form elements have to be defined twice – once in HTML and again in the server side script.
# It is difficult to render the form elements dynamically.
# HTML itself provides no way to validate user's input.
# WTForms is a flexible form rendering and validating library.
# Flask-WTF extension provides a simple interface with this WTForms library.
# Using Flask-WTF,  we can define the form fields in our Python script and render them using an HTML template. It is also possible to apply validation to the WTF field.
# Syntax : pip install flask-WTF
# Flask-WTF contains a Form class, which has to be used as a parent for user- defined form.
# WTforms package contains definitions of various form fields.

# Standard form fields: 

    # TextField: Represents <input type = 'text'> HTML form element

    # BooleanField: Represents <input type = 'checkbox'> HTML form element

    # DecimalField: Textfield for displaying number with decimals

    # IntegerField: TextField for displaying integer

    # RadioField: Represents <input type = 'radio'> HTML form element

    # SelectField: Represents select form element

    # TextAreaField: Represents <testarea> html form element

    # PasswordField: Represents <input type = 'password'> HTML form element

    # SubmitField: Represents <input type = 'submit'> form element

# Example, a form containing a text field 
# from flask_wtf import Form
# from wtforms import TextField

# class ContactForm(Form):
#    name = TextField("Name Of Student")

# In addition to the ‘name’ field, a hidden field for CSRF token is created automatically. 
# This is to prevent Cross Site Request Forgery attack.
# Is equivalent to a HTML file and looks like:  
             # <input id = "csrf_token" name = "csrf_token" type = "hidden" />
             # <label for = "name">Name Of Student</label><br>
             # <input id = "name" name = "name" type = "text" value = "" />

# WTForms package also contains validator class. It is useful in applying validation to form fields.
    # DataRequired : Checks whether input field is empty
    
    # Email: Checks whether text in the field follows email ID conventions
    
    # IPAddress: Validates IP address in input field
    
    # Length: Verifies if length of string in input field is in given range
    
    # NumberRange:Validates a number in input field within given range
    
    # URL: Validates URL entered in input field

# Example: apply ‘DataRequired’ validation rule for the name field in contact form.
    # Syntax: name = TextField("Name Of Student",[validators.Required("Please enter your name.")])

# The validate() function of form object validates the form data and throws the validation errors if validation fails. 
# The Error messages are sent to the template. In the HTML template, error messages are rendered dynamically.
                                                           
# Validators are applied to the Name and Email fields.
                                                           
from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form = form)
        

if __name__ == '__main__':
    app.run(debug = True)

