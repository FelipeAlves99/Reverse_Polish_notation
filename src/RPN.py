import argparse
import Extensions as calc

# Used to specify the .txt path that will be used
# Usado para especificar o arquivo que será usado
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Caminho do arquivo texto")
args = vars(ap.parse_args())

file = open(args["file"], "r")
lines = file.readlines()
lineCalc = []
error = ""

print('+'.isalnum())


resultFile = Open()
for line in lines:
    for char in line:
        if char.isnumeric():
            lineCalc.append(char)

        elif char.isspace():
            continue

        else:
            error = calc.CalculateRPN(char, lineCalc)

        if error is not "":
            WriteLine(
                resultFile, "{} => Result: {}".format(line, error))
            break

    WriteLine(resultFile, "{} => Result: {}".format(line, lineCalc[0]))

Close(resultFile)
print("Processo concluído, arquivo 'result.txt' gerado dentro da pasta 'src' do projeto")


def Open():
    file = open("result.txt", "w+")
    return file


def Close(file):
    file.close()


def WriteLine(file, line):
    file.write("{} \r\n".format(line))
