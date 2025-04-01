import unittest
from half_adder import half_adder


class TestHalfAdder(unittest.TestCase):
    def test_half_adder_logic(self):
        """Test all possible valid inputs (truth table)."""
        test_cases = [
            (0, 0, (0, 0)),  # 0 + 0 = sum: 0, carry: 0
            (0, 1, (1, 0)),  # 0 + 1 = sum: 1, carry: 0
            (1, 0, (1, 0)),  # 1 + 0 = sum: 1, carry: 0
            (1, 1, (0, 1)),  # 1 + 1 = sum: 0, carry: 1
        ]

        for x, y, expected in test_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(half_adder(x, y), expected)

    def test_invalid_inputs(self):
        """Test invalid inputs to ensure function raises ValueError."""
        invalid_cases = [
            (-1, 0), (2, 1), (1, 3),  # Out of range values
            (0.5, 1), ("a", 0), (None, 1)  # Invalid types
        ]

        for x, y in invalid_cases:
            with self.subTest(x=x, y=y):
                with self.assertRaises(ValueError):
                    half_adder(x, y)

    def test_boundary_cases(self):
        """Test extreme boundary cases."""
        self.assertEqual(half_adder(0, 0), (0, 0))  # Both zero
        self.assertEqual(half_adder(1, 1), (0, 1))  # Both one


if __name__ == "__main__":
    unittest.main()
