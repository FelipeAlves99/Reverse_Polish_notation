# Arquivo de extensão para separar o calculo do processo principal
# Extension file to separate the calculation from the main process
def CalculateRPN(char, list):
    if char is '+':
        Add(list)
    elif char is '-':
        Subtract(list)
    elif char is 'x' or '*':
        Multiply(list)
    elif char is '/':
        Divide(list)

# método para adicionar os dois últimos números
# method to add the last two numbers


def Add(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber + lastNumber
    list.append(result)

# método para subtrair os dois últimos números
# method to subtract the last two numbers


def Subtract(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber - lastNumber
    list.append(result)

# método para multiplicar os dois últimos números
# method to multiply the last two numbers


def Multiply(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber * lastNumber
    list.append(result)

# método para dividir os dois últimos números
# method to divide the last two numbers


def Divide(list):
    lastNumber = list.pop()
    secondLastNumber = list.pop()

    result = secondLastNumber / lastNumber
    list.append(result)
