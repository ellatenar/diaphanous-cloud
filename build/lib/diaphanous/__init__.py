from flask import Flask

# url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
# db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
# schema = "schema.sql"
# conn = psycopg.connect(db)

app = Flask(__name__)

import diaphanous.views