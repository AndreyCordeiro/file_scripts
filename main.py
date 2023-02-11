def clear_file() -> str:
    return ""


with open("contratacoes_banco_do_agricultor.txt", "r") as file:
    string = ""
    array = []

    for i in file:
        array = i.replace("\n", "").split(";")

        string += "("

        for value in array:
            if not value.isnumeric():
                aux = value
                replaced = value[:-2]

                if replaced != "":
                    if replaced[-1] == ",":
                        value = aux.replace(",", ".")

                if value == "":
                    value = "';'"

            string += value + ","

        string = string[:-1] + ""

        string += "),\n"

    with open("output.txt", "w") as outputFile:
        outputFile.write(clear_file())
        outputFile.write(string)
