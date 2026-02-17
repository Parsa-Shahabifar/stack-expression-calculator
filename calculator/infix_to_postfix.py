"""
IDEA:
Infix to Postfix conversion module.

NOTE:
Implements stack-based conversion algorithm
to handle operator precedence and parentheses.
Supports: +, -, *, /, ^ and ()
"""

import re
from .checking_priority import check_priority,operators
from .stack import Stack

def Infix_To_Postfix(value:str):
    """
    Convert an infix mathematical expression
    into postfix (Reverse Polish Notation).

    Args:
        value (str): Infix expression

    Returns:
        str: Postfix expression
    """
    seperated_value = re.findall(r'\d+|[^\d\s]', value)
    stack_instance = Stack()
    postfix = ""
    for i in seperated_value:
        if(i.isdigit()):
            postfix += i + " "
        elif(i == "("):
            stack_instance.push(i)
        elif(i == ")"):
            while stack_instance.size() > 0 and stack_instance.peek() != "(":
                postfix += stack_instance.pop() + " "
            stack_instance.pop()
        else :
            while (
                stack_instance.size() > 0 and
                stack_instance.peek() in operators and
                check_priority(stack_instance.peek(), i)
            ):
                postfix += stack_instance.pop() + " "
            stack_instance.push(i)
    while stack_instance.size() > 0:
        postfix += stack_instance.pop()
    return postfix