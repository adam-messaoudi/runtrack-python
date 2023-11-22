def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non valide"

# Exemples d'appels
result = calcule(5, '+', 3)
print(result)

result = calcule(10, '*', 2)
print(result)
