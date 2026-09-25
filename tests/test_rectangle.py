import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from rectangle import area, perimeter
EPSILON = 0.001

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(5, 4)
        self.assertEqual(res, 20)

    def test_perimeter_zero_a(self):
        res = perimeter(0, 18)
        self.assertEqual(res, 36)

    def test_perimeter_positive(self):
        res = perimeter(8, 4)
        self.assertEqual(res, 24)

    def test_perimeter_positive_real(self):
        res = perimeter(10.2, 4.329)
        self.assertAlmostEqual(res, 29.058, delta=EPSILON)

    def test_area_positive_real(self):
        res = area(99.12, 105.987)
        self.assertAlmostEqual(res, 10_505.43144, delta=EPSILON)

    def test_area_negative(self):
        self.assertRaises(ValueError, area, -1, 8)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter, -2, 9)


if __name__ == "__main__":
    unittest.main()
        
