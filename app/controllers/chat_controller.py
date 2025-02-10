from flask import Blueprint, request, jsonify
from app.models.rag_model import RAGModel

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        question = data.get('text', '')
        
        # Use RAG model to generate response
        response = RAGModel.generate_response(question)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500