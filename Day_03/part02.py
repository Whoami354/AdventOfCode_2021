with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    horizontal_input = [''.join(row[i] for row in input) for i in range(len(input[0]))]

most_common = ""
least_common = ""




