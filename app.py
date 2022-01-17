# paypal publicly available sandbox account info
# sandbox info will be replaced when we go live
from secret import SECRET
ACCOUNT = 'sb-pfjzb10622070@business.example.com'
CLIENT_ID = 'AZ8xw20dA9qOb6GHVX1ezMSTmFOyBKHdD4CgHjsJ54gHbADFzjfMz0U8bngjMOiVcheNkR0q4Vy8wJ0R'

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Class(es)
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "really_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

