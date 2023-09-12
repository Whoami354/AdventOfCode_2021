with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    input = [''.join(row[i] for row in input) for i in range(len(input[0]))]

most_common = ""
least_common = ""

for binary in input:
    if binary.count('1') > binary.count('0'):
        most_common += "1"
        least_common += "0"
    else:
        most_common += "0"
        least_common += "1"

print(int(most_common,2)*int(least_common, 2))