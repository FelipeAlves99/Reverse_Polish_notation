def CalculateRPN(char, list):
    if char is '+':
        Add(list)
    elif char is '-':
        Subtract(list)
    elif char is 'x' or '*':
        Multiply(list)
    elif char is '/':
        Divide(list)


def Add(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber + lastNumber
    list.append(result)


def Subtract(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber - lastNumber
    list.append(result)


def Multiply(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber * lastNumber
    list.append(result)


def Divide(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber / lastNumber
    list.append(result)
