from flask import Blueprint, jsonify, request

upload_router = Blueprint('upload_router', __name__)

@upload_router.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    # Process the uploaded file
    return jsonify({'message': 'File uploaded successfully'}), 200