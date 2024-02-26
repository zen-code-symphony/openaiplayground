import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ.get("OPENAI_API_KEY")


OPENAI_CLIENT = openai.OpenAI()


def get_completion(prompt: str, model: str = "gpt-4-turbo-preview") -> str | None:
    """Return completion text for the given prompt using the given model."""
    messages = [{"role": "user", "content": prompt}]
    response = OPENAI_CLIENT.chat.completions.create(
        model=model, messages=messages, temperature=0  # type: ignore
    )
    return response.choices[0].message.content


def process_prompt(prompt: str, model: str = "gpt-4-turbo-preview") -> None:
    """Process prompt and print response."""
    print("PROMPT:")
    print(prompt)
    print("*" * 100)
    print("API RESPONSE:")
    response = get_completion(prompt)
    print(response)
