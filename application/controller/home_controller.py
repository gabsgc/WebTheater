from application import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('base.html')