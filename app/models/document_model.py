import fitz  # PyMuPDF
from app.services.embedding_service import EmbeddingService
from langchain_community.vectorstores import FAISS
class DocumentModel:
    vector_store = None  # FAISS vector store

    @staticmethod
    def process_document(file):
        # Extract text from PDF
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = "".join([page.get_text() for page in doc])
        
        # Split text into chunks
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(text)
        
        # Create embeddings and store in FAISS
        embeddings = EmbeddingService.create_embeddings(chunks)

        if DocumentModel.vector_store is None:

            DocumentModel.vector_store = FAISS.from_texts(chunks, embeddings)
        else :
            DocumentModel.vector_store.add_texts(chunks)

