lines = open("input", "r", encoding='utf-8').read().strip().split()
sumIncreased = 0

newLines = []

for i in range(2, len(lines)):
    firstNumber = int(lines[i - 2])
    secondNumber = int(lines[i - 1])
    thirdNumber = int(lines[i])
    newLines.append(firstNumber + secondNumber + thirdNumber)


for i in range(1,len(newLines)):
    firstNumber = newLines[i - 1]
    secondNumber = newLines[i]
    if firstNumber < secondNumber:
        sumIncreased += 1

print(sumIncreased)