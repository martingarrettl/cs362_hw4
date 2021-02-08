import unittest
import garrett_martin_hw4

class TestClass(unittest.TestCase):
#------------------------------------------------------------------------------
# 1.2 Use the unittest module and write any 3 tests that can test out your code
# HINT: Take into consideration tests for checking negative values, type errors, etc.
#------------------------------------------------------------------------------
    def test_posFloatCubeVolume(self):
        self.assertEqual(garrett_martin_hw4.cubeVolume(3.2), 3.2**3)

    def test_negCubeVolume(self):
        self.assertEqual(garrett_martin_hw4.cubeVolume(-3), 27)

    def test_stringCubeVolume(self):
        self.assertEqual(garrett_martin_hw4.cubeVolume("Hello"), "Error: Invalid edge length provided.")
#------------------------------------------------------------------------------
# 2.2 Use the unittest module and wriet any 3 tests that can test out your code
# HINT: Take into consideration tests for checking empty lists, divide by zero, etc.
#------------------------------------------------------------------------------
    def test_listAverage(self):
        self.assertEqual(garrett_martin_hw4.listAverage([1,2,3,4,5]), 3)

    def test_typeListAverage(self):
        self.assertEqual(garrett_martin_hw4.listAverage(2), "Error: Invalid list provided.")

    def test_zeroListAverage(self):
        self.assertEqual(garrett_martin_hw4.listAverage([]), "Error: Invalid list provided.")
#------------------------------------------------------------------------------
# 3.2 Use the unittest module and write any 3 tests that can test out your code
#------------------------------------------------------------------------------
    def test_fullName(self):
        self.assertEqual(garrett_martin_hw4.fullName("Garrett", "Martin"), "Garrett Martin")

    def test_firstFullName(self):
        self.assertEqual(garrett_martin_hw4.fullName(None, "Martin"), "Error: Invalid first name provided")

    def test_typeFullName(self):
        self.assertEqual(garrett_martin_hw4.fullName("Garrett", 12), "Error: Invalid last name provided")

if __name__ == "__main__":
    unittest.main()
