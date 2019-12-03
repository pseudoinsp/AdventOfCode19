def readInputByLines():
    operations = []
    with open('input.txt') as fin:
            ops = fin.read().split(',')

            for op in ops:
                operations.append(int(op))

    return operations

def calculateProgramResult(operations):
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

    return operations[0]

def searchParametersForOutput(operations, maxValueofVariablesExclusive, searchedOutput):
    
    for currentNoun in range(maxValueofVariablesExclusive):
        for currentVerb in range(maxValueofVariablesExclusive):
            opCopy = operations.copy()
            opCopy[1] = currentNoun
            opCopy[2] = currentVerb

            if(calculateProgramResult(opCopy) == searchedOutput):
                return opCopy[1], opCopy[2]

    return -1, -1


operations = readInputByLines()

noun, verb = searchParametersForOutput(operations, 100, 19690720)

print(f"Part 2: 100*noun + verb: {100*noun+verb}");

