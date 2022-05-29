from flask import render_template
from app import app



@app.route('/')
def startPage():
    return render_template('index.html')