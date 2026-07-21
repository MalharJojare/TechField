import os
from dotenv import load_dotenv


load_dotenv()


class Config:

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    GIPHY_API_KEY = os.getenv(
        "GIPHY_API_KEY"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )
    
    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1-mini"
    )

config = Config()