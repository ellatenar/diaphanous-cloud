from flask import render_template
from flask import request

import psycopg
import urllib.parse
import os

from diaphanous import app

url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg.connect(db)

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
        # Send as SQL Query
        with conn.cursor() as cur:
            name = request.form.get('name')
            email = request.form.get('email')
            if email is not None:
                SQL = "INSERT INTO contacts (name, email) VALUES (%s, %s)"  # Note: no quotes
                data = (name, email)
                cur.execute(SQL, data)
                conn.commit()
                return render_template('confirmed.jinja', subpage=True, title='thank you!')
            else:
                return render_template('signup.jinja', subpage=True, title="please enter an email address <3")
    else:
        return render_template('signup.jinja', subpage=True, title='mailing list')

    
@app.errorhandler(404)
def page_note_found(error):
    return render_template('404.jinja', subpage=True, title='404 not found'), 404