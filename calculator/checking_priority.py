operators = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

def check_priority(operator1 , operator2):
    return operators[operator1] >= operators[operator2] 
