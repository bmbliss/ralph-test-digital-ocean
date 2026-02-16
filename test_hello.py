import unittest
from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        """Test that greet returns the correct greeting."""
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_with_different_name(self):
        """Test that greet works with different names."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")


if __name__ == "__main__":
    unittest.main()
