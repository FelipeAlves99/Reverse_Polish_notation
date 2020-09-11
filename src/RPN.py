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

file = open(args["file"], "r")
lines = file.readlines()
lineCalc = []
error = []


def open_file():
    file = open("result.txt", "w+")
    return file


def Close(file):
    file.close()


def WriteLine(file, line):
    file.write("{} \n".format(line))


resultFile = open_file()
for line in lines:

    if line.isspace():
        WriteLine(resultFile, "")
        continue

    line = re.sub('\r?\n', '', line)

    for char in line:
        if char.isnumeric():
            lineCalc.append(int(char))

        elif char.isspace():
            continue

        elif char.isalpha():
            if char is not 'x':
                error.append('O caracter {} é inválido'.format(char))
                break
            else:
                calc.CalculateRPN(char, lineCalc)

        else:
            calc.CalculateRPN(char, lineCalc)

    if len(lineCalc) > 1:
        error.append('Linha inconsistente, não retornou apenas um resultado. Resultado: {}'.format(
            lineCalc))

    if len(error) > 0:
        WriteLine(
            resultFile, "{} => Result: {}".format(line, error[0]))

    else:
        WriteLine(resultFile, "{} => Result: {}".format(line, lineCalc[0]))

    lineCalc.clear()
    error.clear()

Close(resultFile)
print("Processo concluído, arquivo 'result.txt' gerado dentro da pasta 'src' do projeto")
