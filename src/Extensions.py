def CalculateRPN(char, list):
    print(char)
    if char is '+':
        Add(list)
    elif char is '-':
        Subtract(list)
    elif char is 'x' or '*':
        Multiply(list)
    elif char is '/':
        Divide(list)
    else:
        return "A linha possui um caracter invalido: {}".format(char)

    return ""


def Add(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(secondLastNumber) + int(lastNumber)
    list.append(result)


def Subtract(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(secondLastNumber) - int(lastNumber)
    list.append(result)


def Multiply(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(secondLastNumber) * int(lastNumber)
    list.append(result)


def Divide(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = int(secondLastNumber) / int(lastNumber)
    list.append(result)
