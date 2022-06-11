from flask import render_template
from app import app
from app import tsession


@app.route('/')
@app.route('/StartPage/')
def startPage():
    return render_template('index.html', code=tsession["regim"])