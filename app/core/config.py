import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", None)

# Database
DB_URL = os.getenv("DB_URL", None)
DB_NAME = os.getenv("DB_NAME", None)
DB_COLLECTION_PRODUCT = os.getenv("DB_COLLECTION_PRODUCT", None)

# Playwright
PLAYWRIGHT_HEADLESS = True
PLAYWRIGHT_IGNORE_HTTPS_ERRORS = False