def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Invalid operator"

print(calcule(1, '+', 2))
