from calculator.infix_to_postfix import Infix_To_Postfix
from calculator.postfix_to_resault import Postfix_to_Answer

def main(value: str):
    postfix = Infix_To_Postfix(value)
    result = Postfix_to_Answer(postfix)
    return result


if __name__ == "__main__":
    print("------- Welcome To Engineer Calculator Project --------")
    user_input = input("Enter The Value : ")
    print("Result:", main(user_input))
