import unittest
from full_adder import full_adder


class TestFullAdder(unittest.TestCase):
    def test_full_adder_logic(self):
        """Test all possible valid inputs (truth table)."""
        test_cases = [
            (0, 0, 0, (0, 0)),  # 0 + 0 + 0 = 00
            (0, 0, 1, (1, 0)),  # 0 + 0 + 1 = 01
            (0, 1, 0, (1, 0)),  # 0 + 1 + 0 = 01
            (0, 1, 1, (0, 1)),  # 0 + 1 + 1 = 10
            (1, 0, 0, (1, 0)),  # 1 + 0 + 0 = 01
            (1, 0, 1, (0, 1)),  # 1 + 0 + 1 = 10
            (1, 1, 0, (0, 1)),  # 1 + 1 + 0 = 10
            (1, 1, 1, (1, 1)),  # 1 + 1 + 1 = 11
        ]

        for A, B, Cin, expected in test_cases:
            with self.subTest(A=A, B=B, Cin=Cin):
                self.assertEqual(full_adder(A, B, Cin), expected)

    def test_invalid_inputs(self):
        """Test invalid inputs to ensure the function raises errors."""
        invalid_cases = [
            (-1, 0, 0), (2, 1, 0), (1, 1, 3),  # Out of range values
            (0.5, 1, 0), ("a", 0, 1), (None, 1, 0)  # Wrong types
        ]

        for A, B, Cin in invalid_cases:
            with self.subTest(A=A, B=B, Cin=Cin):
                with self.assertRaises(ValueError):
                    full_adder(A, B, Cin)

    def test_boundary_cases(self):
        """Test edge cases with repeated values."""
        self.assertEqual(full_adder(0, 0, 0), (0, 0))  # All zero
        self.assertEqual(full_adder(1, 1, 1), (1, 1))  # All one

    def test_randomized_cases(self):
        """Test a mix of inputs to ensure consistent behavior."""
        self.assertEqual(full_adder(1, 1, 0), (0, 1))
        self.assertEqual(full_adder(0, 1, 1), (0, 1))
        self.assertEqual(full_adder(1, 0, 1), (0, 1))


if __name__ == "__main__":
    unittest.main()
