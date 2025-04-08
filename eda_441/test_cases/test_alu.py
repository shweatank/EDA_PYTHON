import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
import random


@cocotb.test()
async def test_alu_with_ml_learning(dut):
    """Test ALU operations and train ML model on ALU behavior"""

    from sklearn.tree import DecisionTreeClassifier
    import numpy as np

    # ML training data
    X = []
    Y = []

    # Test vector format: (A, B, ALU_Sel, Expected Output, CarryOut)
    test_vectors = [
        (0b0011, 0b0001, 0b000, 0b0110, 0),  # A + B
        (0b1111, 0b0001, 0b000, 0b0000, 1),  # A + B (overflow)
        (0b0100, 0b0001, 0b001, 0b0011, 0),  # A - B
        (0b0011, 0b0101, 0b010, 0b0001, 0),  # A & B
        (0b0011, 0b0101, 0b011, 0b0111, 0),  # A | B
        (0b0011, 0b0101, 0b100, 0b0110, 0),  # A ^ B
        (0b1010, 0b0000, 0b101, 0b0101, 0),  # ~A
        (0b0011, 0b0000, 0b110, 0b0110, 0),  # A << 1
        (0b1010, 0b0000, 0b111, 0b0101, 0),  # A >> 1
    ]

    for A, B, sel, expected_out, expected_carry in test_vectors:
        dut.A.value = A
        dut.B.value = B
        dut.ALU_Sel.value = sel

        await Timer(10, units="ns")

        actual_out = int(dut.ALU_Out.value)
        actual_carry = int(dut.CarryOut.value)

        # Append features and label for ML model
        features = [A, B, sel]
        X.append(features)
        Y.append(actual_out)  # You could train separate model for carry too

        # Regular assertion test
        assert actual_out == expected_out, \
            f"ALU_Out mismatch: A={A:04b}, B={B:04b}, Sel={sel:03b}, Got={actual_out:04b}, Expected={expected_out:04b}"
        assert actual_carry == expected_carry, \
            f"CarryOut mismatch: A={A:04b}, B={B:04b}, Sel={sel:03b}, Got={actual_carry}, Expected={expected_carry}"

    # Train and evaluate ML model
    model = DecisionTreeClassifier()
    model.fit(np.array(X), np.array(Y))
    acc = model.score(X, Y)

    cocotb.log.info(f"ML Model trained on ALU behavior with accuracy: {acc:.4f}")
