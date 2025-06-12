from flask import Flask

# Import Blueprints
from ..routes.health_router import health_router
from ..routes.upload_router import upload_router

def register_blueprints(app):
    """
    Register the Blueprints to the Flask application.
    """
    app.register_blueprint(health_router)
    app.register_blueprint(upload_router)



