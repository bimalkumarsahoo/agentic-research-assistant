from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("GEMINI_API_KEY") == None:
    raise Exception("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
