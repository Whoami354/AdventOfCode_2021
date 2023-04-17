lines = open("input", "r", encoding='utf-8').read().strip().split()
sumIncreased = 0


for i in range(1 ,len(lines)):
    firstNumber = int(lines[i - 1])
    secondNumber = int(lines[i])
    if firstNumber < secondNumber:
        sumIncreased += 1

print(sumIncreased)
