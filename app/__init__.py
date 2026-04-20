from flask import Flask
from app.extensions import db, cors
from app.config import Config

# Import all route blueprints
from app.routes.user_routes import user_bp
from app.routes.course_routes import course_bp
from app.routes.enrollment_routes import enrollment_bp
from app.routes.assignment_routes import assignment_bp
from app.routes.submission_routes import submission_bp
from app.routes.grade_routes import grade_bp


def create_app():
    app = Flask(__name__, static_folder='../static', static_url_path='')

    # Load config
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)

    # Register Blueprints (API routes)
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(course_bp, url_prefix='/api')
    app.register_blueprint(enrollment_bp, url_prefix='/api')
    app.register_blueprint(assignment_bp, url_prefix='/api')
    app.register_blueprint(submission_bp, url_prefix='/api')
    app.register_blueprint(grade_bp, url_prefix='/api')

    # Serve frontend
    @app.route('/')
    def home():
        return app.send_static_file('elms.html')

    # Create DB tables
    with app.app_context():
        db.create_all()

    return app