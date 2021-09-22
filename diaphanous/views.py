from flask import render_template

from diaphanous import app

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/sound/")
@app.route("/audio/")
def sound():
    return render_template('audio.html')

@app.route("/hi")
def about():
    return render_template('hi.html')

@app.errorhandler(404)
def page_note_found(error):
    return render_template('404.html'), 404