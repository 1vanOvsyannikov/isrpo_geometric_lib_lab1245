import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from square import area, perimeter
EPSILON = 0.001

class SquareTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(15)
        self.assertEqual(res, 225)

    def test_perimeter_zero_a(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_positive_real(self):
        res = perimeter(7.6342)
        self.assertAlmostEqual(res, 30.5368, delta=EPSILON)

    def test_area_positive_real(self):
        res = area(3.3329)
        self.assertAlmostEqual(res, 11.10822241, delta=EPSILON)

    # def test_area_negative(self):
    #     self.assertRaises(ValueError, area, -1)

    # def test_perimeter_negative(self):
    #     self.assertRaises(ValueError, perimeter, -2)

if __name__ == "__main__":
    unittest.main()
        
        
