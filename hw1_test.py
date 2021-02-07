import unittest 
import hw1

class Triangle_test(unittest.TestCase):

    def test1(self):
        self.assertEqual(hw1.classify_triangle(3,4,5), "The triangle is scalene and right")
    def test2(self):
        self.assertEqual(hw1.classify_triangle(2,2,2), "The triangle is equilateral")
    def test3(self):
        self.assertEqual(hw1.classify_triangle(1,1,2), "The triangle is isosceles")
if __name__ == '__main__':
    unittest.main()
 