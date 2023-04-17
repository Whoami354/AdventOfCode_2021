lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
sumForward = 0
sumY = 0

for line in lines:
    direction = line[:line.find(" ")]
    distance = int(line[line.rfind(" ") + 1:])
    if direction == "forward":
        sumForward += distance
    elif direction == "up":
        sumY -= distance
    elif direction == "down":
        sumY += distance

print(sumForward * sumY)