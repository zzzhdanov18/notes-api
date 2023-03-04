import os
from dotenv import load_dotenv

load_dotenv()

a = os.getenv("MAIN_DATABASE_URL")
print(a)