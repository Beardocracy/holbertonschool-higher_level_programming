#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = len(sys.argv)
    if args != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    operands = ['+', '-', '*', '/']
    operator = sys.argv[2]
    good_operator = False
    for op in operands:
            if operator == op:
                    good_operator = True
    if not good_operator:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (operator == '+'):
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
    elif (operator == '-'):
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
    elif (operator == '*'):
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
    elif (operator == '/'):
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
