import math
import unittest
import circle
import rectangle
import square
import triangle
from circle import perimeter


class TestAllFunctions(unittest.TestCase):
    #Checking for circle

    def test_AreaCircle_valid(self):
        self.assertAlmostEqual(circle.area(6), math.pi* 36, places=6)
    def test_PerimeterCircle_valid(self):
        self.assertAlmostEqual(circle.perimeter(6), math.pi * 12, places = 6)
    def test_AreaCircle_value(self):
        with self.assertRaises(ValueError):
            circle.area(0)
            circle.area(-10)
    def test_AreaCircle_type(self):
        with self.assertRaises(TypeError):
            circle.area("stringtype")
            circle.area(5.20)
    def test_PerimeterCircle_value(self):
        with self.assertRaises(ValueError):
            circle.perimeter(0)
            circle.perimeter(-10)
    def test_PerimeterCircle_type(self):
        with self.assertRaises(TypeError):
            circle.perimeter("stringtype")
            circle.perimeter(5.20)

    def test_PerimeterCircle_large(self):
        with self.assertRaises(ValueError):
            circle.perimeter(1_000_000_001)

    def test_PerimeterCircle_smalles(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1_000_000_001)

    def test_AreaCircle_large(self):
        with self.assertRaises(ValueError):
            circle.area(1_000_000_001)

    def test_AreaCircle_smalles(self):
        with self.assertRaises(ValueError):
            circle.area(-1_000_000_001)


    #Checking for rectangle
    def test_AreaRectangle_valid(self):
        self.assertAlmostEqual(rectangle.area(3,5),15)
    def test_PerimeterRectangle_valid(self):
        self.assertAlmostEqual(rectangle.perimeter(3,5),16)
    def test_AreaRectangle_value(self):
        with self.assertRaises(ValueError):
            rectangle.area(0,5)
            rectangle.area(6,0)
            rectangle.area(-3,5)
            rectangle.area(6,-8)
    def test_PerimeterRectangle_value(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(0,5)
            rectangle.perimeter(6,0)
            rectangle.perimeter(-3,5)
            rectangle.perimeter(6,-8)
    def test_AreaRectangle_type(self):
        with self.assertRaises(TypeError):
            rectangle.area("lol",5)
            rectangle.area(8.15,20)
    def test_PerimeterRectangle_type(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("lol",5)
            rectangle.perimeter(8.15,20)
    def test_AreaRectangle_large(self):
        with self.assertRaises(ValueError):
            rectangle.area(1_000_000_001,5)

    def test_PerimeterRectangle_large(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(1_000_000_001,5)

    def test_AreaRectangle_smalles(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1_000_000_001,5)

    def test_PerimeterRectangle_smalles(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1_000_000_001,5)


    #Checking for square
    def test_AreaSquare_valid(self):
        self.assertAlmostEqual(square.area(5),25)
    def test_PerimeterSquare_valid(self):
        self.assertAlmostEqual(square.perimeter(5),20)
    def test_AreaSquare_value(self):
        with self.assertRaises(ValueError):
            square.area(0)
            square.area(-100)
    def test_PerimeterSquare_value(self):
        with self.assertRaises(ValueError):
            square.perimeter(0)
            square.perimeter(-100)
    def test_AreaSquare_type(self):
        with self.assertRaises(TypeError):
            square.area("lol")
            square.area(8.15)
    def test_PerimeterSquare_type(self):
        with self.assertRaises(TypeError):
            square.perimeter("lol")
            square.perimeter(8.15)
    def test_AreaSquare_large(self):
        with self.assertRaises(ValueError):
            square.area(1_000_000_001)
    def test_PerimeterSquare_large(self):
        with self.assertRaises(ValueError):
            square.perimeter(1_000_000_001)
    def test_AreaSquare_smalles(self):
        with self.assertRaises(ValueError):
            square.area(-1_000_000_001)
    def test_PerimeterSquare_smalles(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1_000_000_001)


    #Checking for triangle
    def test_AreaTriangle_valid(self):
        self.assertAlmostEqual(triangle.area(10,2),10)
    def test_PerimeterTriangle_valid(self):
        self.assertAlmostEqual(triangle.perimeter(10, 5,5), 20)
    def test_AreaTriangle_value(self):
        with self.assertRaises(ValueError):
            triangle.area(0,5)
            triangle.area(-100,8)
    def test_PerimeterTriangle_value(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0,5,0)
            triangle.perimeter(-100,8,0)
    def test_AreaTriangle_type(self):
        with self.assertRaises(TypeError):
            triangle.area("lol",10)
            triangle.area(8.15,10)
    def test_PerimeterTriangle_type(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("lol",10,2.5)
            triangle.perimeter(8.15,10,"da")
    def test_AreaTriangle_large(self):
        with self.assertRaises(ValueError):
            triangle.area(1_000_000_001,20)
    def test_PerimeterTriangle_large(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1_000_000_001,20,40)
    def test_AreaTriangle_smalles(self):
        with self.assertRaises(ValueError):
            triangle.area(-1_000_000_001,20)
    def test_PerimeterTriangle_smalles(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-1_000_000_001,20,50)


if __name__ == '__main__':
    unittest.main()