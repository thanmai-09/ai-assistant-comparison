import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("models/gemini-2.0-flash")

def get_frontier_response(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        return "Frontier Assistant is temporarily unavailable due to API quota limits."