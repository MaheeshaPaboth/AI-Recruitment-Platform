import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key is missing!")
    exit()

client = genai.Client(api_key=api_key)

try:

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Say Hello in one sentence."
    )

    print("Gemini connection successful!")
    print(response.text)

except Exception as e:

    print("Gemini connection failed!")
    print("Error:", repr(e))

finally:

    client.close()
