import os

API_ID    = os.environ.get("API_ID", "23035668")
API_HASH  = os.environ.get("API_HASH", "37e73a238b2258a1294cdbd63e4e934f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
