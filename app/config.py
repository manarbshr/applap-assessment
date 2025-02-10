from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Validate required keys
    @classmethod
    def validate(cls):
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is missing in .env file")