from flask import Flask

# Define a function to create the Flask application
def create_app():
    # Create an instance of the Flask class
    app = Flask(__name__)
    # Set a secret key for the application (used for session management)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .views import views
    from .auth import auth

    # Register the blueprints with the main application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
