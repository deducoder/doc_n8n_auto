import os
import mimetypes
import magic  # python-magic library for file type detection

class FileRecognitionService:
    @staticmethod
    def identify_file_type(file):
        """
        Identifies the type of file based on both extension and content.
        
        Args:
            file: FileStorage object from Flask
            
        Returns:
            dict: Contains file type information including:
                - extension: The file extension
                - mime_type: The MIME type
                - content_type: The content type based on file magic numbers
                - category: General category of the file
        """
        # Get the file extension
        filename = file.filename
        extension = os.path.splitext(filename)[1].lower() if filename else ''
        
        # Get MIME type based on extension
        mime_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        
        # Read the file content for magic number analysis
        file_content = file.read()
        # Reset file pointer to beginning for subsequent operations
        file.seek(0)
        
        # Use python-magic to detect file type from content
        content_type = magic.from_buffer(file_content, mime=True)
        
        # Determine general category
        category = FileRecognitionService._determine_category(mime_type, content_type)
        
        return {
            'extension': extension,
            'mime_type': mime_type,
            'content_type': content_type,
            'category': category
        }
    
    @staticmethod
    def _determine_category(mime_type, content_type):
        """
        Determines the general category of the file based on MIME type.
        """
        if mime_type.startswith('image/'):
            return 'image'
        elif mime_type.startswith('video/'):
            return 'video'
        elif mime_type.startswith('audio/'):
            return 'audio'
        elif mime_type in ['application/pdf']:
            return 'document'
        elif mime_type in ['application/msword', 
                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                         'application/vnd.ms-excel',
                         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            return 'office_document'
        elif mime_type.startswith('text/'):
            return 'text'
        else:
            return 'other'
