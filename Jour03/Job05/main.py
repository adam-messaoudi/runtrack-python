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

# Exemples d'appels de la fonction
result = calcule(5, '+', 3)
print(result)

result = calcule(10, '*', 2)
print(result)

result = calcule(5, '-', 3)
print(result)

result = calcule(10, '=', 2)
print(result)

result = calcule(-65, '/', 3)
print(result)

result = calcule(15, '%', 7)
print(result)


