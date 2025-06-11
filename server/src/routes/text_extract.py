from flask import Blueprint, jsonify

text_extract_router = Blueprint("text_extract_router", __name__)


@text_extract_router.route("/text_extract")
def text_extraction():
    """
    Text extraction endpoint.
    """
    response = {"message": "Endpoint working"}
    return jsonify(response), 200
