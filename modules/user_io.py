import csv


def userReader(file: str):
    with open("{file}", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            break


def userWriter(
    file: str, modeAppend: str, atribute1: str, typeOperation: str, atribute2: str
):
    with open({file}, {modeAppend}, newline="") as f:
        writer = csv.writer(f)
        writer.writerow([{atribute1}, {typeOperation}, {atribute2}])


def userWriter(
    file: str, modeWriter: str, atribute1: str, atribute2: str, atribute3: str
):
    with open({file}, {modeWriter}, newline="") as f:
        writer = csv.writer(f)
        writer.writerow([{atribute1}, {atribute2}, {atribute3}])
