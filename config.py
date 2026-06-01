import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-it-in-production')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    
    # Database configuration
    # Default to sqlite relative to base dir if not set or sqlite format is specified
    db_url = os.environ.get('DATABASE_URL', '')
    if not db_url:
        db_url = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'stock_predictor.db')}"
    elif db_url.startswith('sqlite:///database/'):
        db_url = db_url.replace('sqlite:///database/', f"sqlite:///{os.path.join(BASE_DIR, 'database')}/")
    
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Directories
    DATABASE_DIR = os.path.join(BASE_DIR, 'database')
    UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')
    ML_MODELS_DIR = os.path.join(BASE_DIR, 'ml_models')
    
    # Ensure standard directories exist
    os.makedirs(DATABASE_DIR, exist_ok=True)
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    os.makedirs(ML_MODELS_DIR, exist_ok=True)
    
    # API configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    
    # Prediction config
    AUTO_RETRAIN = os.environ.get('AUTO_RETRAIN', 'true').lower() == 'true'
