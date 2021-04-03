# A web based application is often required to have a feature of sending mail to the users/clients.
# Firstly, Flask-Mail extension has to be installed with the help of pip utility.
# Syntax: pip install Flask-Mail
# or download the latest version from version control:
        # git clone https://github,com/mattupstate/flask-mail.git
        # cd flask-mail
        # python setup.py install
# The Flask-Mail needs to be configured by setting values of following application parameters.
    # MAIL_SERVER : Name/IP address of email server.
    # MAIL_PORT : Port Number of server used.
    # MAIL_USE_TLS : Enable/Disable Tranport Security Layer Encryption.
    # MAIL_USE_SSL : Enable/Disable SSL encryption.
    # MAIL_DEBUG : Debug Support.
    # MAIL_USERNAME: User Name and Password of sender.
    # MAIL_PASSWORD : --- SAME AS ABOVE ---
    # MAIL_DEFAULT_SENDER : Sets default sender.
    # MAIL_MAX_SEND : Sets maximum mails to be sent.
    # MAIL_SUPPRESS_SEND : Sending suppressed if app.testing set to true.
    # MAIL_ASCII_ATTAVHMENTS : If True, attached filenames converted to ASCII.

# Mail Class: It manages email messaging requirements. The class constructor takes following form.
# Syntax : flask-mail.Mail(app=None)

# Mail class Methods:
    # send() : Sends contents of Message class object
    # connect() : Opens connecttion with mail host
    # send_message() : Sends message object.
# Message class :It encapsulates an email message. Message class constructor has several parameters −
    # Syntax: flask-mail.Message(subject, recipients, body, html, sender, cc, bcc, 
    # reply-to, date, charset, extra_headers, mail_options, rcpt_options)  
    
# Message class methods: 
    # attach() − adds an attachment to message. This method takes the following parameters −
          # filename : name of file to attach
          # content_type : MIME type of file
          # data : raw file data
          # disposition : content disposition, if any.

    # add_recipient() − adds another recipient to message 

# ---------CODE------------    

# Step 1- Import Mail and Message class from flask-mail module in the code.    
# from flask_mail import Mail, Message

# Step 2 − Then Flask-Mail is configured as per following settings.
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# Step 3 − Create an instance of Mail class.
# mail = Mail(app)

# Step 4 − Set up a Message object in a Python function mapped by URL rule (‘/’).
# @app.route("/")
# def index():
   # msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
   # msg.body = "This is the email body"
   # mail.send(msg)
   # return "Sent"

# Challenges:
# Built-in Security features in Gmail service may block this login attempt. 
# You may have to decrease the security level. Please log in to your Gmail account 
# and visit this link to decrease the security.
# Link : https://www.google.com/settings/security/lessecureapps  

from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sakvrn1234@gmail.com'
app.config['MAIL_PASSWORD'] = 'SV@123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender = 'sakvrn1234@gmail.com', recipients = ['varun.sakunia@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)
