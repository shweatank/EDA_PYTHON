# Find Cocotb installation path
COCOTB := $(shell python3 -c 'import cocotb; print(cocotb.__path__[0])')

# Verilog source files
VERILOG_SOURCES := nand_gate.v

# Define the top-level Verilog module
TOPLEVEL := nand_gate

# Define the Python testbench module (without .py)
MODULE := test_nand_gate_cocotb

# Select the simulator (Icarus Verilog)
SIM := icarus

# Enable VCD Dump (change 'waves' to your preferred filename)
export WAVES=1

# Include Cocotb Makefile
include $(COCOTB)/share/makefiles/Makefile.sim
