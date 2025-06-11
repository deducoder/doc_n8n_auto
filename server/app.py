from flask import Flask, jsonify
import config
from src.routes.main_router import register_blueprints

# Initialize Flask application
app = Flask(__name__)

# Import Blueprints from main_router
register_blueprints(app)

if __name__ == "__main__":
    # Use the configurations to run and listen the Flask app
    app.run(host=str(config.HOST), port=config.PORT, debug=config.DEBUG)