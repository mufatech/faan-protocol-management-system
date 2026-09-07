from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

# FIXED URI (IMPORTANT)
app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Simple test model (use an existing table OR temporary model)
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)

@app.route('/test-database')
def test_database_connection():
    try:
        result = db.session.execute(db.text("SELECT 1")).fetchone()
        return f"Database Connection Successful! Result: {result}"
    except Exception as e:
        return f"Database Connection Failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)