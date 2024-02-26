"""Demonstrate instructing model to work out its own solution before rushing to
a conclusion.

This technique is based on the prompting principle:
Give the model time to "think".
"""

from app.common.prompt_processor import process_prompt


def get_no_instruct_prompt() -> str:
    """Ask for verification without instructing to work out own solution."""
    prompt = """
    Determine if the student's solution is correct or not.

    Question:
    I'm building a solar power installation and I need
    help working out the financials.
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost
    me a flat $100k per year, and an additional $10 / square
    foot
    What is the total cost for the first year of operations
    as a function of the number of square feet.

    Student's Solution:
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    """
    return prompt


def get_instruct_prompt() -> str:
    """Ask for verification by instructing to work out own solution."""
    prompt = """
    Your task is to determine if the student's solution
    is correct or not.
    To solve the problem do the following:
    - First, work out your own solution to the problem including the final
      total.
    - Then compare your solution to the student's solution
    and evaluate if the student's solution is correct or not.
    Don't decide if the student's solution is correct until
    you have done the problem yourself.

    Use the following format:
    Question:
    ```
    question here
    ```
    Student's solution:
    ```
    student's solution here
    ```
    Actual solution:
    ```
    steps to work out the solution and your solution here
    ```
    Is the student's solution the same as actual solution
    just calculated:
    ```
    yes or no
    ```
    Student grade:
    ```
    correct or incorrect
    ```

    Question:
    ```
    I'm building a solar power installation and I need help
    working out the financials.
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost
    me a flat $100k per year, and an additional $10 / square
    foot
    What is the total cost for the first year of operations
    as a function of the number of square feet.
    ```
    Student's solution:
    ```
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    ```
    Actual solution:
    """
    return prompt


if __name__ == "__main__":
    print("ASK VERIFICATION WITHOUT WORKING OUT A SOLUTION:")
    process_prompt(get_no_instruct_prompt())
    print("\n\n\nASK VERIFICATION AFTER WORKING OUT A SOLUTION:")
    process_prompt(get_instruct_prompt())
