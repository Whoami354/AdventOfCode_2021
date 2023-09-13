from copy import deepcopy

with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

oxygen_diagnostics = deepcopy(input)

for i in range(len(input[0])):
    if len(oxygen_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxygen_diagnostics]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen_diagnostics) / 2 else '0'
    oxygen_diagnostics = [entry for entry in oxygen_diagnostics if entry[i] == common_bit]

oxygen_rating = int(oxygen_diagnostics[0], 2)

co2_diagnostic = deepcopy(input)

for i in range(len(input[0])):
    if len(co2_diagnostic) == 1:
        break

    all_entries_at_pos = [entry[i] for entry in co2_diagnostic]
    least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2_diagnostic) / 2 else '1'

    co2_diagnostic = [entry for entry in co2_diagnostic if entry[i] == least_common_bit]

co2_rating = int(co2_diagnostic[0], 2)
print(co2_rating*oxygen_rating)
