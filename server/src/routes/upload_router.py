from flask import Blueprint, jsonify, request
from ..services.file_recognition import FileRecognitionService

upload_router = Blueprint('upload_router', __name__)

@upload_router.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Identify the file type
    try:
        file_info = FileRecognitionService.identify_file_type(file)
        
        # Here you can add additional processing based on file type
        # For example, validate allowed file types, scan for viruses, etc.
        
        return jsonify({
            'message': 'File uploaded successfully',
            'file_info': file_info
        }), 200
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 400