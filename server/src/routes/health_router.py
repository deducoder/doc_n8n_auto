from flask import Blueprint, jsonify
import config

health_router = Blueprint("health_router", __name__)


@health_router.route("/health")
def health():
    """
    Health check endpoint to verify the server and configuration status.
    """
    response = {
        "status": "success",
        "message": "Server is health",
        "host": config.HOST,
        "port": config.PORT,
        "debug": config.DEBUG,
    }
    return jsonify(response), 200
