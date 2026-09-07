from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from dotenv import load_dotenv
from config import Config
import os



load_dotenv(override=True)

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
login_manager = LoginManager()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app():

    app = Flask(__name__)

    # Load config
    app.config.from_object(Config)


    # Override from env (if needed)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['UPLOAD_FOLDER'] = os.path.join(
    BASE_DIR,
    'static',
    'uploads'
)
    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'login_page'


    # Import models (IMPORTANT: after db init)
    from app.models.admin import Admin
    from app.models.user import User
    from app.models.forms import (
        Organization,
        Passenger,
        ServiceLevel,
        SpecialNeed,
        passenger_special_needs,
        
    )

    # Register blueprints (IMPORTANT)
    from app.routes.root import root_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp

    app.register_blueprint(root_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    return app


