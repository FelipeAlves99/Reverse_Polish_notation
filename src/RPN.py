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
isvalid = True


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
    else:
        WriteLine(resultFile, "{} => Result: {}".format(line, lineCalc[0]))

    lineCalc.clear()

Close(resultFile)
print("Processo concluído, arquivo 'result.txt' gerado dentro da pasta 'src' do projeto")
