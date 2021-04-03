# Flask is referred to as a micro framework.
# Core functionality includes WSGI and routing based on Werkzeug and template engine based on Jinja2.
# In addition Flask framework has support for cookie and sessions as well as helpers like JSON, static files, etc.
# Obviously this is not enough for development of full fledged web application.
# A Flask extension is a Python module which adds specific type of support to Flask application.
# Flask Extension Registry is a directory of extesions available.
# Required extension can be downloaded by pip utility.
# Flask Mail : Provides SMTP interface to Flask application.
# Flask WTF : Adds rendering and validation of WTForms.
# Flask SQLAlchemy : Adds SQLAlchemy support to Flask application.
# Flask Sijax : Interface for Sijax - Python/jQuery library that makes AJAX easy to use in web applications.
# Since an extension is a Python module, it needs to be imported for it to be used.
# Flask extensions are generally named as flask-foo.
# Syntax: from flask_foo import [class, function]
# For various versions of Flask later than 0.7, you can also use the Syntax : from flask.ext import foo
# For this usage, a compatibility module needs to be activated. It can be installed by running flaskext_compat.py

import flaskext_compat
flaskext_compat.activate()
from flask.ext import foo
