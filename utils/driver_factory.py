from dotenv import load_dotenv
import os

load_dotenv()

def get_base_url():
    return os.getenv("BASE_URL")