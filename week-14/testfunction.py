import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test case class
class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)  # Assertion to check if 3 + 5 = 8

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -7), -10)  # Assertion to check if -3 + -7 = -10

    def test_add_zero_to_number(self):
        self.assertEqual(add(10, 0), 10)  # Assertion to check if 10 + 0 = 10

unittest.main()