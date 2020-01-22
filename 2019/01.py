
with open("01.txt") as f:
    lines = f.read().splitlines()

def calcFuel(mass):
    fuel = int(mass)//3-2
    return fuel if fuel > 0 else 0

fuels = list(map(calcFuel, lines))

part1 = sum(fuels)
part2 = 0
while (sum(fuels) > 0):
    part2 += sum(fuels)
    fuels = list(map(calcFuel, fuels))

print(part1)
print(part2)