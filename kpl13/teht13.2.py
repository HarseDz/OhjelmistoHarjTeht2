import mysql.connector
from flask import Flask
app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta(icao):
    try:

