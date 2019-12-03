def readInputByLines():
    operations = []
    with open('input.txt') as fin:
            ops = fin.read().split(',')

            for op in ops:
                operations.append(int(op))

    return operations

operations = readInputByLines()

operations[1] = 12;
operations[2] = 2;

currentOpIndex = 0
while True:
    if(operations[currentOpIndex] == 99):
        break

    operand = operations[currentOpIndex]
    firstOpIndex = operations[currentOpIndex + 1]
    secondOpIndex = operations[currentOpIndex + 2]
    targetIndex = operations[currentOpIndex + 3]

    if(operand == 1):
        operations[targetIndex] = operations[firstOpIndex] + operations[secondOpIndex]
    elif(operand == 2):
        operations[targetIndex] = operations[firstOpIndex] * operations[secondOpIndex]

    currentOpIndex += 4

print(f"Part 1: first number in operations: {operations[0]}");

