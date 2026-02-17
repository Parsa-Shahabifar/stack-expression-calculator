import re
from .stack import Stack


def Postfix_to_Answer(postfixed_value: str):
    """
    Evaluate a postfix (Reverse Polish Notation) expression
    using a stack-based algorithm.

    Args:
        postfixed_value (str): Postfix expression

    Returns:
        int: Final evaluated result
    """

    stack_instance = Stack()
    seperated_value = re.findall(r'\d+|[^\d\s]', postfixed_value)

    for token in seperated_value:

        if token.isdigit():
            stack_instance.push(int(token))

        else:
            right = stack_instance.pop()
            left = stack_instance.pop()

            if token == "+":
                stack_instance.push(left + right)

            elif token == "-":
                stack_instance.push(left - right)

            elif token == "*":
                stack_instance.push(left * right)

            elif token == "/":
                stack_instance.push(left / right)

            elif token == "^":
                stack_instance.push(left ** right)

            else:
                raise ValueError("Invalid operator in postfix expression")

    return stack_instance.peek()
