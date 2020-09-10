import argparse
import Extensions as calc
import WriteResult as writer

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


resultFile = writer.Open()
for line in lines:
    for char in line:
        if char.isnumeric():
            lineCalc.append(char)

        elif char.isspace():
            continue

        else:
            error = calc.CalculateRPN(char, lineCalc)

        if error is not "":
            writer.WriteLine(
                resultFile, "{} => Result: {}".format(line, error))
            break

    writer.WriteLine(resultFile, "{} => Result: {}".format(line, lineCalc[0]))

writer.Close(resultFile)
print("Processo concluído, arquivo 'result.txt' gerado dentro da pasta 'src' do projeto")
