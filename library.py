from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routes

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

if __name__ == '__main__':
    routes.app.run(debug=True)
