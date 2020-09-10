def CalculateRPN(char, list):
    if char is '+':
        Add(list)
    if char is '-':
        Subtract(list)
    if char is '*':
        Multiply(list)
    if char is '/':
        Divide(list)
    else:
        return "A linha possui um caracter invalido: {}".format(char)

    return ""


def Add(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(lastNumber) + int(secondLastNumber)
    list.append(result)


def Subtract(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(lastNumber) - int(secondLastNumber)
    list.append(result)


def Multiply(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(lastNumber) * int(secondLastNumber)
    list.append(result)


def Divide(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(lastNumber) / int(secondLastNumber)
    list.append(result)
