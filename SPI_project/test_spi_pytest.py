import pytest
import csv
import os

def simulate_spi_transfer(data_in):
    """
    Simulates SPI Master transmission for an 8-bit input.
    Outputs a MOSI bitstream for the input.
    """
    mosi_bits = ""
    sclk = 0

    for i in range(8):  # 8-bit data
        for _ in range(2):  # SCLK toggles twice per bit
            sclk ^= 1  # Toggle clock
            if sclk:  # On rising edge
                bit = (data_in >> (7 - i)) & 1
                mosi_bits += str(bit)

    done = 1
    return mosi_bits, done

# Load test cases from CSV
def load_csv_cases():
    file_path = os.path.join(os.path.dirname(__file__), "spi_testcases.csv")
    test_cases = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_in = int(row["data_in"])
            expected_mosi = row["expected_mosi"]
            test_cases.append((data_in, expected_mosi))
    return test_cases

@pytest.mark.parametrize("data_in,expected_mosi", load_csv_cases())
def test_spi_transfer_csv(data_in, expected_mosi):
    mosi_out, done = simulate_spi_transfer(data_in)

    assert done == 1, f"Transfer not marked done for input {data_in:#02x}"
    assert mosi_out == expected_mosi, f"Expected MOSI={expected_mosi}, Got={mosi_out}"
    print(f"✅ Passed: data_in={data_in:#04x}, MOSI={mosi_out}")
