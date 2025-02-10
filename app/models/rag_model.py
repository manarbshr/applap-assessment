from app.services.embedding_service import EmbeddingService
from app.services.gemini_service import GeminiService
from app.models.document_model import DocumentModel

class RAGModel:
    @staticmethod
    def generate_response(question):
        if not DocumentModel.vector_store:
            raise ValueError("Upload a document first!")
        
        # Retrieve relevant context
        docs = DocumentModel.vector_store.similarity_search(question, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        
        # Generate answer using Gemini
        prompt = f"""Answer this question: {question}
        Using only this context: {context}
       "."""
        
        return GeminiService.generate_response(prompt)