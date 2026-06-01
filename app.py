import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from config import Config
from models import db
from models.user import User
from routes.auth import auth_bp
from routes.main import main_bp
from routes.api import api_bp
from routes.admin import admin_bp

csrf = CSRFProtect()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)

    # Setup User Loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('base.html', content_only=True), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('base.html', content_only=True), 500

    # Ensure database tables exist
    with app.app_context():
        db.create_all()
        # Seed an admin user if not present (admin/adminpass)
        if User.query.filter_by(username='admin').first() is None:
            admin_user = User(username='admin', email='admin@antigravity.ai')
            admin_user.set_password('admin123')
            admin_user.is_admin = True
            db.session.add(admin_user)
            db.session.commit()
            print("Default admin user created: admin / admin123")

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
