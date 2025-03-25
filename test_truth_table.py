import pytest
def truth_table():
    and_table = [(a, b, a & b) for a in [0, 1] for b in [0, 1]]
    or_table = [(a, b, a | b) for a in [0, 1] for b in [0, 1]]
    not_table = [(a, 1 - a) for a in [0, 1]]
    return and_table, or_table, not_table


result_and = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
result_or = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
result_not = [(0, 1), (1, 0)]

@pytest.mark.parametrize("a, b, expected", result_and)
def test_and_gate(a, b, expected):
    assert (a & b) == expected, f"Failed for {a} AND {b}"

@pytest.mark.parametrize("a, b, expected", result_or)
def test_or_gate(a, b, expected):
    assert (a | b) == expected, f"Failed for {a} OR {b}"

@pytest.mark.parametrize("a, expected", result_not)
def test_not_gate(a, expected):
    assert (1 - a) == expected, f"Failed for NOT {a}"

if __name__ == "__main__":
    pytest.main()


