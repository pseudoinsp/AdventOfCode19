import math

def calculateRequiredFuel(mass):
    fuel = (math.floor(mass / 3)) - 2
    return fuel

def readInputByLines():
    lines = []
    with open('input.txt') as fin:
        for line in fin:
            lineAsString = line.strip()
            lines.append(int(lineAsString))

    return lines

lines = readInputByLines()

sum = 0;

for number in lines:
    sum += calculateRequiredFuel(number);

print(f"Part 1: sum fuel required: {sum}");

sum = 0;

for number in lines:
    while number > 0:
        fuelRequired = calculateRequiredFuel(number)

        if(fuelRequired < 0):
            break;
        else:
            sum += fuelRequired;
            number = fuelRequired;    
    
print(f"Part 2: sum fuel required: {sum}");