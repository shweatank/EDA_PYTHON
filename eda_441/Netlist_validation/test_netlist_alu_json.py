import json
import unittest

def load_alu_json(json_path):
    with open(json_path, 'r') as f:
        netlist = json.load(f)
    return netlist

def simulate_add(a, b):
    return (a + b) & 0xF  # 4-bit wraparound

def simulate_sub(a, b):
    return (a - b) & 0xF

def simulate_and(a, b):
    return a & b

def simulate_or(a, b):
    return a | b

class TestALUFromJSON(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.netlist = load_alu_json("alu.json")

    def test_add(self):
        result = simulate_add(0b0001, 0b0011)
        self.assertEqual(result, 0b0011)

    def test_sub(self):
        result = simulate_sub(0b0101, 0b0010)
        self.assertEqual(result, 0b0011)

    def test_and(self):
        result = simulate_and(0b0001, 0b0011)
        self.assertEqual(result, 0b0001)

    def test_or(self):
        result = simulate_or(0b0001, 0b0010)
        self.assertEqual(result, 0b0011)

    def test_netlist_has_basic_cells(self):
        cells = self.netlist['modules']['alu']['cells']
        cell_types = {cell['type'] for cell in cells.values()}
        expected = {'$_AND_', '$_OR_', '$_XOR_', '$_MUX_'}
        missing = expected - cell_types
        self.assertTrue(len(missing) == 0, f"Missing logic gates: {missing}")

# Custom test runner to print summary
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestALUFromJSON)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    passed = result.testsRun - len(result.failures) - len(result.errors)
    failed = len(result.failures) + len(result.errors)

    print("\n" + "="*40)
    print(f"✅ Total Passed: {passed}")
    print(f"❌ Total Failed: {failed}")
    print("="*40)
