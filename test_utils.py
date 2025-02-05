import unittest
from utils import sum_numbers, is_palindrome, factorial, is_even

class TestUtils(unittest.TestCase):

    def test_sum_numbers(self):
        """Test sum_numbers() with positive and negative values."""
        self.assertEqual(sum_numbers(5, 7), 12)
        self.assertEqual(sum_numbers(-5, -7), -12)
        self.assertEqual(sum_numbers(-3, 2), -1)

    def test_is_palindrome(self):
        """Test is_palindrome() function."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_factorial(self):
        """Test factorial() function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-3)  # Negative values should raise an error

    def test_is_even(self):
        """Test is_even() function."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(99))

if __name__ == '__main__':
    unittest.main()
