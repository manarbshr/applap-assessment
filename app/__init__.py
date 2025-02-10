from flask import Flask, render_template
from flask_cors import CORS

def create_app():
    # Configure template and static folders inside "view"
    app = Flask(
        __name__,
        template_folder='view/templates',  # Path to templates
        static_folder='view/static'        # Path to static files
    )
    CORS(app)
    
    # Serve the home page
    @app.route('/')
    def home():
        return render_template('index.html')  # Renders index.html from templates
    
    # Register blueprints (controllers)
    from app.controllers.chat_controller import chat_bp
    from app.controllers.upload_controller import upload_bp
    app.register_blueprint(chat_bp)
    app.register_blueprint(upload_bp)
    
    return app