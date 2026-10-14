import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from circle import area, perimeter
EPSILON = 0.001

class CircleTestCase(unittest.TestCase):
    def test_area_zero_rad(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_random_pos_rad_area(self):
        res = area(7)
        self.assertAlmostEqual(res, 153.938040026, delta=EPSILON)

    def test_perimeter_zero_rad(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_random_pos_rad_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.8318530718, delta=EPSILON)

    def test_perimeter_positive_real(self):
        res = perimeter(5.555)
        self.assertAlmostEqual(res, 34.9030943814, delta=EPSILON)

    def test_area_positive_real(self):
        res = area(64.333)
        self.assertAlmostEqual(res, 13_002.2191224, delta=EPSILON)

    def test_area_negative(self):
        self.assertRaises(ValueError, area, -1)

    # def test_perimeter_negative(self):
    #     self.assertRaises(ValueError, perimeter, -2)


if __name__ == "__main__":
    unittest.main()
    