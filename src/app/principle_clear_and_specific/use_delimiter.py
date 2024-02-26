"""Demonstrate usage of delimiters to indicate distinct parts of the input.

This technique is based on the prompting principle:
Write clear and specific instructions.

Note: delimiters can be anything e.g. ```, \"\"\", < >, <tag> </tag> etc. In
this example, we used ``` i.e. triple backticks as the delimiter.
"""

from app.common.prompt_processor import process_prompt


def get_delimit_prompt() -> str:
    """Use delimiters to clearly indicate distinct parts of the input."""
    text = """
    You should express what you want a model to do by
    providing instructions that are as clear and
    specific as you can possibly make them.
    This will guide the model towards the desired output,
    and reduce the chances of receiving irrelevant
    or incorrect responses. Don't confuse writing a
    clear prompt with writing a short prompt.
    In many cases, longer prompts provide more clarity
    and context for the model, which can lead to
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks into a single sentence.
    ```{text}```
    """
    return prompt


if __name__ == "__main__":
    process_prompt(get_delimit_prompt())
