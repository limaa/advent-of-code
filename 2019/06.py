from collections import defaultdict
from typing import List, Dict
import logging
import os


class Planet(object):
    def __init__(self):
        self.parent = ""
        self.children = []
        self.name = ""


def generate_orbit_map(map_data: List[str]) -> Dict[str, Planet]:
    orbit_map = defaultdict(Planet)
    for data in map_data:
        planet1, planet2 = data.split(')')
        orbit_map[planet1].name = planet1
        orbit_map[planet1].children.append(planet2)
        orbit_map[planet2].name = planet2
        orbit_map[planet2].parent = planet1

    return orbit_map


def calculate_orbit_checksum(orbit_map: Dict[str, Planet]) -> int:
    orbit_checksum = 0
    levels_deep = 0
    current_planet = 'COM'
    logging.debug(f'Orbit map')
    logging.debug(orbit_map)

    def calc_checksum_recursive(orbit_map: Dict[str, Planet],
                                current_planet: str,
                                levels_deep: int):
        children = orbit_map[current_planet].children
        planet_checksum = levels_deep

        logging.debug(f'--------------------------')
        logging.debug(f'Calculating checksum')
        logging.debug(f'Planet: {current_planet}')
        logging.debug(f'Levels deep: {levels_deep}')

        for child in children:
            child_checksum = calc_checksum_recursive(
                orbit_map,
                child,
                levels_deep+1)
            planet_checksum += child_checksum
            logging.debug(f'Child checksum: {child_checksum}')

        logging.debug(f'Total checksum for planet {current_planet} is '
                      f'{planet_checksum}')
        return planet_checksum

    orbit_checksum = calc_checksum_recursive(
        orbit_map,
        current_planet,
        levels_deep)
    return orbit_checksum


def find_path_to_com(orbit_map: Dict[str, Planet], planet: str):
    parents = []
    current_planet = planet
    while orbit_map[current_planet].parent != '':
        current_planet = orbit_map[current_planet].parent
        parents.append(current_planet)
    return parents


if __name__ == '__main__':
    INPUT = '06.txt'
    TEST_INPUT = '06_test.txt'
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # logging.basicConfig(level=logging.DEBUG)
    # FILE_INPUT = os.path.join(SCRIPT_DIR, TEST_INPUT)
    FILE_INPUT = os.path.join(SCRIPT_DIR, INPUT)

    with open(FILE_INPUT) as f:
        map_data = f.read().splitlines()

    orbit_map = generate_orbit_map(map_data)
    path_me_com = find_path_to_com(orbit_map, 'YOU')
    path_santa_com = find_path_to_com(orbit_map, 'SAN')
    path_me_santa = [
        planet
        for planet in path_me_com
        if planet not in path_santa_com
        ] + [
        planet for planet in path_santa_com if planet not in path_me_com]
    print(f'Part 1: {calculate_orbit_checksum(orbit_map)}')
    print(f'Part 2: {len(path_me_santa)}')
