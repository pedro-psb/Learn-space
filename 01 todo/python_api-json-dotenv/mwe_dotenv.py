from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv('KEY')
print(KEY)
