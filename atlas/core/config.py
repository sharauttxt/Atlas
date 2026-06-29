from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5-coder:7b")