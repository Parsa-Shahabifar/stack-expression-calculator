import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.infix_to_postfix import Infix_To_Postfix
from calculator.postfix_to_resault import Postfix_to_Answer

def test_basic_operations():
    assert Postfix_to_Answer(Infix_To_Postfix("(10+2)*5-15")) == 45
    assert Postfix_to_Answer(Infix_To_Postfix("10*(20-4*3)")) == 80
    assert Postfix_to_Answer(Infix_To_Postfix("5+3-48*2")) == -94


if __name__ == "__main__":
    test_basic_operations()
