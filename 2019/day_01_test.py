import unittest
import day_01


class TestDay01(unittest.TestCase):
    def test_fuel_calculation(self):
        self.assertEqual(day_01.calc_fuel(12), 2)
        self.assertEqual(day_01.calc_fuel(14), 2)
        self.assertEqual(day_01.calc_fuel(1969), 654)
        self.assertEqual(day_01.calc_fuel(100756), 33583)

    def test_recursive_fuel_calculation(self):
        self.assertEqual(day_01.calc_fuel_recursive(14), 2)
        self.assertEqual(day_01.calc_fuel_recursive(1969), 966)
        self.assertEqual(day_01.calc_fuel_recursive(100756), 50346)


if __name__ == '__main__':
    unittest.main()
