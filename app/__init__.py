from flask import Flask, render_template, stream_with_context, Response, request, Markup
from playhouse.flask_utils import FlaskDB,  object_list, get_object_or_404
from datetime import date, timedelta
import os

ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.environ['DATABASE_URL']
DEBUG = False
SECRET_KEY = 'shhh, secret!'  # Used by Flask to encrypt session cookie.
SITE_WIDTH = 800

birthday = date(2006, 1, 11)
today = date.today()

age = (today - birthday)/ timedelta(365)
age = "14+" if age > int(age) else "14"

app = Flask(__name__)
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database
