from flask import Flask

# Import health Blueprint
from src.routes.health_router import health_router

def register_blueprints(app):
    """
    Register the Blueprints to the Flask application.
    """
    app.register_blueprint(health_router)