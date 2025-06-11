from flask import Flask

# Import Blueprints
from ..routes.health_router import health_router
from ..routes.text_extract import text_extract_router


def register_blueprints(app):
    """
    Register the Blueprints to the Flask application.
    """
    app.register_blueprint(health_router)
    app.register_blueprint(text_extract_router)
