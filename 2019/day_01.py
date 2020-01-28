import os


def calc_fuel(mass: int) -> int:
    fuel = mass//3-2
    return fuel if fuel > 0 else 0


def calc_fuel_recursive(mass: int) -> int:
    current_fuel = calc_fuel(mass)
    total_fuel = current_fuel
    while current_fuel > 0:
        current_fuel = calc_fuel(current_fuel)
        total_fuel += current_fuel
    return total_fuel


if __name__ == '__main__':
    INPUT = 'day_01_input.txt'
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_INPUT = os.path.join(SCRIPT_DIR, INPUT)

    with open(FILE_INPUT) as f:
        masses = list(map(int, f.read().splitlines()))

    part1 = sum(list(map(calc_fuel, masses)))
    part2 = sum(list(map(calc_fuel_recursive, masses)))

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
