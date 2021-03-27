from flask import Blueprint, render_template
import os


views = Blueprint('views', __name__)

@views.route('/')
def landing():
	return '<script>window.location.href="/auth"</script>'

@views.route('/home')
def home():
	s = ''
	with (open('.todo', 'r')) as file:
		for i in file.readlines():
			s += i.replace('<', '&lt;')
	return f'<pre>{s}</pre>'
