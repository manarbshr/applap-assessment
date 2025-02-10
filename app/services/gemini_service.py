from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import Config


class GeminiService:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=Config.GOOGLE_API_KEY)

    @staticmethod
    def generate_response(prompt):
        return GeminiService.llm.invoke(prompt).content