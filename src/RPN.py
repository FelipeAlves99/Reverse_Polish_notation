# Nome: Felipe de Carvalho Alves
# RA: N2864F-5

import argparse
import Extensions as calc
import re

# Used to specify the .txt path that will be used
# Usado para especificar o arquivo que será usado
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Caminho do arquivo texto")
args = vars(ap.parse_args())

# Opens the file and read the lines
# Abre o arquivo e lê as linhas
file = open(args["file"], "r")
lines = file.readlines()

# Variables declaration
# Declaralçao de variaveis
lineCalc = []
error = []

# Method to create a new file to save all equation results
# Método para criar um novo arquivo para salvar o resultado de todas as equações


def open_file():
    file = open("result.txt", "w+")
    return file

# method to close the result file
# Método para fechar o arquivo de resultados


def Close(file):
    file.close()

# Method to write the lines in the result file
# Método para escrever as linhas no arquivo de resultado


def WriteLine(file, line):
    file.write("{} \n".format(line))

# Method to call the extension script and calculate (or try to) the line equation
# Método para chamar o script de extensão e calcular (ou tentar) a equação da linha


def Calculate(char, lineCalc):
    try:
        calc.CalculateRPN(char, lineCalc)
    except:
        error.append(
            'Linha com erro de calculo')


# Process start
# Inicio do processo
resultFile = open_file()

# To each line of the file lines, do something
# Para cada linha das linhas do arquivo, faça algo
for line in lines:

    # If the line is blank/empty, jump to the next line
    # Se for apenas uma linha em branco, pular o processamento
    if line.isspace():
        WriteLine(resultFile, "")
        continue

    # Remove the break line symbol at the end of the line
    # Remove quebra linha presente no final da linha
    line = re.sub('\r?\n', '', line)

    # To each char in the line, do something
    # Para cada caracter da linha, faça algo
    for char in line:

        # Keeps all chars lower case
        # Deixa todos os caracteres minusculos
        char.lower()

        # If the char is numeric, add to calculation list
        # Se o caracter for numérico, adiciona para a lista de calculo
        if char.isnumeric():
            lineCalc.append(int(char))

        # If the char is a space, jump to the next char
        # Se o caracter for um espaço, pula para o próximo caracter
        elif char.isspace():
            continue

        # If the char is alphabetic and NOT x, return an invalid char error
        # Se o caracter for alfabético e não ser X, retornar um erro de caracter inválido
        elif char.isalpha():
            if char is not 'x':
                error.append('O caracter {} é inválido'.format(char))
                break

            # Execute the calculation when the char is x
            # Efetua o calculo quando o caracter for x
            else:
                Calculate(char, lineCalc)

        # Execute the calculation when is a special char
        # Efetua o calculo sempre que for algum caracter especial
        else:
            Calculate(char, lineCalc)

    # If the calculation list has more than one value, add an error for that line
    # Se a lista de calculos tiver mais de um valor, adiciona um erro para aquela linha
    if len(lineCalc) > 1:
        error.append('Linha inconsistente, não retornou apenas um resultado. Resultado: {}'.format(
            lineCalc))

    # If the error list has an error, write the error in the result file
    # Se a lista de erros tiver algum erro, escreva o erro no arquivo de resultado
    if len(error) > 0:
        WriteLine(
            resultFile, "{} => ERRO: {}".format(line, error[0]))

    # If the error list has 0 items, write the line result in the result file
    # Se a lista de erros for 0, escreva o resultado da linha no arquivo de resultados
    else:
        WriteLine(resultFile, "{} => Result: {}".format(line, lineCalc[0]))

    # Clear the calcualtion list and error list
    # Limpa as listas de calculo e erro da linha
    lineCalc.clear()
    error.clear()

# Close the result file and ends the script
# Fecha o arquivo de resultado e finaliza o script
Close(resultFile)
print("Processo concluído, arquivo 'result.txt' gerado dentro da pasta 'src' do projeto")
