from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import FAISS



class EmbeddingService:
    @staticmethod
    def create_embeddings(chunks):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        return embeddings