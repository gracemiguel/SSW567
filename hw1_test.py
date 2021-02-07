import unittest 
import hw1

class Triangle_test(unittest.TestCase):

    def test1(self):
        self.assertEqual(hw1.classify_triangle(3,4,5), "The triangle is scalene and right")
    def test2(self):
        self.assertEqual(hw1.classify_triangle(2,2,2), "The triangle is equilateral")
    def test3(self):
        self.assertEqual(hw1.classify_triangle(1,1,2), "The triangle is isosceles")
    def test4(self):
        self.assertRaises(TypeError, hw1.classify_triangle("hi", "peeps", "two"))
    def test5(self):
        self.assertRaises(TypeError, hw1.classify_triangle(1,2,3))
    def test6(self): 
        self.assertNotEqual(hw1.classify_triangle(5, 5, 7), "This is a scalene triangle")

if __name__ == '__main__':
    unittest.main()
    
 