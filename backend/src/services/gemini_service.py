# backend/src/services/gemini_service.py
import os
import google.generativeai as genai
from typing import List
from ..models.data_models import Chunk

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_answer(self, query: str, chunks: List[Chunk]) -> str:
        """
        Generates an answer to a query using the Gemini API, based on the provided chunks.
        """
        context = "\n\n".join([chunk.text for chunk in chunks])
        prompt = f"""
        Context:
        {context}

        Question:
        {query}

        Answer:
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating answer with Gemini: {e}")
            return "I am sorry, but I was unable to generate an answer."
