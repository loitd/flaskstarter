from flask import Flask, Blueprint
from jinja2 import TemplateNotFound
from secrets import token_hex
import json, config
from views.findex import findex_blpr
from waitress import serve
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# Create new Flask application with instance_relative_config
app = Flask(__name__, instance_relative_config=True)
# register blueprint
app.register_blueprint(findex_blpr)
# read configs from files
app.config.from_object('config')
app.config.from_pyfile('config.py')
# define database to use SQLAlchemy
db = SQLAlchemy(app)
# debug toolbar
toolbar = DebugToolbarExtension(app)

if __name__ == '__main__':
	app.run(debug=True, threaded=True, host='localhost', port=5000)
	# serve(app, host='localhost', port=8000)