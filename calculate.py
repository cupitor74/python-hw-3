import sys

left_operand = ''
operation = '' 
right_operand = ''

if len(sys.argv) > 4 and len(sys.argv) != 2:
    print('Arg len should be 4')
    sys.exit()

elif len(sys.argv) == 2:
    value = sys.argv[1]
    allowed_operations = ['+', '-', '/', '*', '%']
    for operand in allowed_operations:
        if operand in value:
            values = value.split(operand)
            if len(values) != 2:
                print('String contains many operands')
                sys.exit()
            if len(values) == 2:
                left_operand = values[0]
                operation = operand
                right_operand = values[1]
else:
    left_operand = sys.argv[1]
    operation = sys.argv[2]
    right_operand = sys.argv[3]


def calc(left_operand, operation, right_operand):
    allowed_operations = ['+', '-', '/', '*', '%']
    if operation not in allowed_operations:
        print('Operation is not allowed.')
        return
    try:
        left_operand = int(left_operand)
        right_operand = int(right_operand)
    except ValueError:
        print('Left and Right operands must be int')
        return
    if operation == '/' and right_operand == 0:
        print('Division by zero is not allowed')
        return
    match operation:
        case '+': 
            return print(left_operand + right_operand)
        case '-': 
            return print(left_operand - right_operand)
        case '/': 
            return print(left_operand / right_operand)
        case '*': 
            return print(left_operand * right_operand)
        case '%': 
            return print(left_operand % right_operand)

calc(left_operand, operation , right_operand)