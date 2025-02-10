from flask import Blueprint, request, jsonify
from app.models.document_model import DocumentModel

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_pdf():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
            
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        # Process and store the document
        DocumentModel.process_document(file)
        return jsonify({"status": "Document processed successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500