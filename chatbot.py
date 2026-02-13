"""
Chatbot module for Career Guidance Chatbot
Handles Gemini API interaction and response generation
"""

from google import genai
from google.genai import types
from config import API_KEY, MODEL_NAME, SYSTEM_PROMPT


def initialize_gemini_client():
    """Initialize Gemini API client with API key."""
    return genai.Client(api_key=API_KEY)


def _map_role(role):
    """Map Streamlit-style roles to Gemini roles."""
    if role == "assistant":
        return "model"
    return "user"


def generate_response(user_input, client, history=None, system_prompt=None):
    """
    Generate a conversational response from Gemini using chat history.

    Args:
        user_input (str): Current user message
        client (genai.Client): Initialized Gemini client
        history (list[dict] | None): Previous chat messages with keys role/content
        system_prompt (str | None): Optional system instruction override

    Returns:
        str: Response text from the model
    """
    contents = []

    if history:
        # Keep recent turns to preserve context while controlling token usage.
        for msg in history[-12:]:
            role = _map_role(msg.get("role", "user"))
            text = (msg.get("content") or "").strip()
            if not text:
                continue
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=text)],
                )
            )

    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],
        )
    )

    config = types.GenerateContentConfig(
        system_instruction=system_prompt or SYSTEM_PROMPT,
        temperature=0.9,
        top_p=0.95,
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=contents,
        config=config,
    ):
        if chunk.text:
            response += chunk.text

    return response.strip()
