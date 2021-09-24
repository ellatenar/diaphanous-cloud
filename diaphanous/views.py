from flask import render_template
from flask import request

from diaphanous import app

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.jinja', index=True, title='diaphanous cloud')

@app.route("/sound/")
def sound():
    return render_template('audio.jinja', title='selected sound sources')

@app.route("/hi")
def about():
    return render_template('hi.jinja', title='hi')

@app.errorhandler(404)
def page_note_found(error):
    return render_template('404.jinja', title='404 not found'), 404