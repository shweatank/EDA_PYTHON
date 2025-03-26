def test_half_adder():
    test_mat = [[0, 0], [0, 1], [1, 0], [1, 1]]

    expected_sum = [0, 1, 1, 0]
    expected_carry = [0, 0, 0, 1]
    computed_sum = [a ^ b for a, b in test_mat]
    computed_carry = [a & b for a, b in test_mat]

    assert computed_sum == expected_sum, f"SUM Test Failed! Expected {expected_sum}, got {computed_sum}"
    assert computed_carry == expected_carry, f"CARRY Test Failed! Expected {expected_carry}, got {computed_carry}"

    print("All test cases passed!")
test_half_adder()
