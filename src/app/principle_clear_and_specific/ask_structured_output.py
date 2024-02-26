"""Demonstrate asking for a structured output.

This technique is based on the prompting principle:
Write clear and specific instructions.

Note: structured output can be anything e.g. JSON, HTML etc. In
this example, we used JSON as the output format.
"""

from app.common.prompt_processor import process_prompt


def get_structured_outout_prompt() -> str:
    """Ask for a structured output."""
    prompt = """
    Generate a list of three made-up book titles along
    with their authors and genres.
    Provide them in JSON format with the following keys:
    book_id, title, author, genre.
    """
    return prompt


if __name__ == "__main__":
    process_prompt(get_structured_outout_prompt())
