import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from triangle import area, perimeter
EPSILON = 0.001

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(4, 3)
        self.assertAlmostEqual(res, 6, delta=EPSILON)

    def test_perimeter_zero_a_b_c(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_positive_real(self):
        res = perimeter(6.5, 5.333, 8.9)
        self.assertAlmostEqual(res, 20.733, delta=EPSILON)

    def test_area_positive_real(self):
        res = area(7.5, 18.3)
        self.assertAlmostEqual(res, 68.625, delta=EPSILON)

    # def test_area_negative(self):
    #     self.assertRaises(ValueError, area, -1, 8)

    # def test_perimeter_negative(self):
    #     self.assertRaises(ValueError, perimeter, -2, 9, 8)

if __name__ == "__main__":
    unittest.main()
        
