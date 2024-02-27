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


def get_completion_from_messages(
    messages: list[dict],
    model: str = "gpt-4-turbo-preview",
    temperature: int = 0,
    max_tokens: int = 500,
) -> str | None:
    response = OPENAI_CLIENT.chat.completions.create(
        model=model,
        messages=messages,  # type: ignore
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def get_completion_from_messages_and_token_count(
    messages: list[dict],
    model: str = "gpt-4-turbo-preview",
    temperature: int = 0,
    max_tokens: int = 500,
) -> tuple:
    response = OPENAI_CLIENT.chat.completions.create(
        model=model,
        messages=messages,  # type: ignore
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = response.choices[0].message.content
    token_dict = {
        "prompt_tokens": response.usage.prompt_tokens,  # type: ignore
        "completion_tokens": response.usage.completion_tokens,  # type: ignore
        "total_tokens": response.usage.total_tokens,  # type: ignore
    }

    return content, token_dict


def process_prompt(prompt: str, model: str = "gpt-4-turbo-preview") -> None:
    """Process prompt and print response."""
    print("PROMPT:")
    print(prompt)
    print("*" * 100)
    print("API RESPONSE:")
    response = get_completion(prompt)
    print(response)


def process_messages_prompt(
    messages: list[dict], model: str = "gpt-4-turbo-preview", temperature: int = 0
) -> None:
    print("MESSAGES:")
    print(messages)
    print("*" * 100)
    print("API RESPONSE:")
    response = get_completion_from_messages(
        messages=messages, model=model, temperature=temperature
    )
    print(response)


def process_messages_prompt_with_token_count(
    messages: list[dict], model: str = "gpt-4-turbo-preview", temperature: int = 0
) -> None:
    print("MESSAGES:")
    print(messages)
    print("*" * 100)
    print("API RESPONSE:")
    response = get_completion_from_messages_and_token_count(
        messages=messages, model=model, temperature=temperature
    )
    print(response)
