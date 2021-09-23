from flask import render_template

from diaphanous import app

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.jinja', subpage=False, title='diaphanous cloud')

@app.route("/sound/")
def sound():
    return render_template('audio.jinja', subpage=True, title='selected sound sources')

@app.route("/hi")
def about():
    return render_template('hi.jinja', subpage=True, title='hi')

# @app.route("/signup", methods=['POST', 'GET'])
# def signup():
    
@app.errorhandler(404)
def page_note_found(error):
    return render_template('404.jinja', subpage=True, title='404 not found'), 404

# client = pymongo.MongoClient("mongodb+srv://ella:jvu2hpc*frp_wth8DWC@cluster0.jb8cd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test