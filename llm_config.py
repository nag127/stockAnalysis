# llm_config.py

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Set API key securely (optional fallback in code if .env not used)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "sk-YOUR API Key")  # Replace default only during dev

# Create and export LLM
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
