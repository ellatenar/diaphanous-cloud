from flask import render_template
from flask import request

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

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method=='POST':
        # Send into MongoDB
        name = request.form.get('name')
        email = request.form.get('email')
        if email is not None:
            try:
                db.contacts.insert_one({'name': name, 'email': email})
            except:
                return render_template('error.jinja', subpage=True, title='500 error')
        
        return render_template('confirmed.jinja', subpage=True, title='thank you!')
    else:
        return render_template('signup.jinja', subpage=True, title='mailing list')

    
@app.errorhandler(404)
def page_note_found(error):
    return render_template('404.jinja', subpage=True, title='404 not found'), 404