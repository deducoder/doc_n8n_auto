from flask import Flask, jsonify
import config

# Initialize Flask application
app = Flask(__name__)

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify the server and configuration status.
    """
    response = {
        "status": "success",
        "message": "Server is running",
        "host": config.HOST,
        "port": config.PORT,
        "debug": config.DEBUG
    }
    return jsonify(response), 200

# Root endpoint
@app.route("/", methods=["GET"])
def root():
    """
    Root endpoint to verify the server status.
    """
    response = {
        "message": "Online"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    # Use the configurations to run and listen the Flask app
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)