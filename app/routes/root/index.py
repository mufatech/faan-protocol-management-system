from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("root/index.html")
