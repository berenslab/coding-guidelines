from typing import Union


def add_two_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Adds two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Added numbers.
    """
    return a + b


if __name__ == "__main__":
    a = 3
    b = 2

    print(f"Adding two numbers {a} + {b} = {add_two_numbers(a,b)}")
