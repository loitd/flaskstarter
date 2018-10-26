from flask import Flask, jsonify, make_response, abort, request, render_template, Blueprint
from jinja2 import TemplateNotFound

findex_blpr = Blueprint('findex', import_name=__name__, template_folder='templates', static_folder='static')

@findex_blpr.route('/')
def findex_func():
	# try:
	return render_template('findex/index.html', name="findex")
	# except TemplateNotFound:
	# 	return abort(404)