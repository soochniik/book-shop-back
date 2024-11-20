from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from models import db
from routes import books_bp, orders_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

app.register_blueprint(books_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
