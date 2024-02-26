"""Demonstrate specifying steps required to complete a task.

This technique is based on the prompting principle:
Give the model time to "think".
"""

from app.common.prompt_processor import process_prompt


def get_task_specification_prompt() -> str:
    """Use delimiters to clearly indicate distinct parts of the input."""
    text = """
    In a charming village, siblings Jack and Jill set out on
    a quest to fetch water from a hilltop
    well. As they climbed, singing joyfully, misfortune
    struck—Jack tripped on a stone and tumbled
    down the hill, with Jill following suit.
    Though slightly battered, the pair returned home to
    comforting embraces. Despite the mishap,
    their adventurous spirits remained undimmed, and they
    continued exploring with delight.
    """
    prompt = f"""
    Perform the following actions:
    1 - Summarize the following text delimited by triple backticks with
        1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the following keys:
        french_summary, num_names.

    Separate your answers with line breaks.

    Text:
    ```{text}```
    """
    return prompt


def get_task_specification_with_format_prompt() -> str:
    """Use delimiters to clearly indicate distinct parts of the input."""
    text = """
    In a charming village, siblings Jack and Jill set out on
    a quest to fetch water from a hilltop
    well. As they climbed, singing joyfully, misfortune
    struck—Jack tripped on a stone and tumbled
    down the hill, with Jill following suit.
    Though slightly battered, the pair returned home to
    comforting embraces. Despite the mishap,
    their adventurous spirits remained undimmed, and they
    continued exploring with delight.
    """
    prompt = f"""
    Your task is to perform the following actions:
    1 - Summarize the following text delimited by
    <> with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the
    following keys: french_summary, num_names.

    Use the following format:
    Text: <text to summarize>
    Summary: <summary>
    Translation: <summary translation>
    Names: <list of names in summary>
    Output JSON: <json with summary and num_names>

    Text: <{text}>
    """
    return prompt


if __name__ == "__main__":
    print("TASK SPECIFICATION PROMPT:")
    process_prompt(get_task_specification_prompt())
    print("\n\n\nTASK SPECIFICATION WITH FORMAT PROMPT:")
    process_prompt(get_task_specification_with_format_prompt())
