"""Demonstrate "Few-shot" prompting.

This technique is based on the prompting principle:
Write clear and specific instructions.
"""

from app.common.prompt_processor import process_prompt


def get_few_shots_prompt() -> str:
    """Use delimiters to clearly indicate distinct parts of the input."""
    prompt = """
    Your task is to answer in a consistent style.

    <child>: Teach me about patience.

    <grandparent>: The river that carves the deepest
    valley flows from a modest spring; the
    grandest symphony originates from a single note;
    the most intricate tapestry begins with a solitary thread.

    <child>: Teach me about resilience.
    """
    return prompt


if __name__ == "__main__":
    process_prompt(get_few_shots_prompt())
