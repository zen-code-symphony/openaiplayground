"""Demonstrate asking the model to check whether conditions are satisfied.

This technique is based on the prompting principle:
Write clear and specific instructions.
"""

from app.common.prompt_processor import process_prompt


def get_prompt_with_conditions() -> str:
    """Ask the model to check whether conditions are satisfied."""
    text = """
    Making a cup of tea is easy! First, you need to get some
    water boiling. While that's happening,
    grab a cup and put a tea bag in it. Once the water is
    hot enough, just pour it over the tea bag.
    Let it sit for a bit so the tea can steep. After a
    few minutes, take out the tea bag. If you
    like, you can add some sugar or milk to taste.
    And that's it! You've got yourself a delicious
    cup of tea to enjoy.
    """

    prompt = f"""
    You will be provided with text delimited by triple quotes.
    If it contains a sequence of instructions,
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions,
    then simply write \"No steps provided.\"

    \"\"\"{text}\"\"\"
    """

    return prompt


def get_prompt_without_conditions() -> str:
    """Ask the model to check whether conditions are satisfied."""
    text = """
    The sun is shining brightly today, and the birds are
    singing. It's a beautiful day to go for a
    walk in the park. The flowers are blooming, and the
    trees are swaying gently in the breeze. People
    are out and about, enjoying the lovely weather.
    Some are having picnics, while others are playing
    games or simply relaxing on the grass. It's a
    perfect day to spend time outdoors and appreciate the
    beauty of nature.
    """

    prompt = f"""
    You will be provided with text delimited by triple quotes.
    If it contains a sequence of instructions,
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions,
    then simply write \"No steps provided.\"

    \"\"\"{text}\"\"\"
    """

    return prompt


if __name__ == "__main__":
    print("WITH CONDITIONS PROMPT")
    process_prompt(get_prompt_with_conditions())
    print("\n\nWITHOUT CONDITIONS PROMPT")
    process_prompt(get_prompt_without_conditions())
