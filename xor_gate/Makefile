# Locate Cocotb
COCOTB := $(shell python3 -c 'import cocotb; print(cocotb.__path__[0])')

# Verilog Source File
VERILOG_SOURCES = xor_gate.v
TOPLEVEL = xor_gate
MODULE = test_xor
SIM = icarus  # Using Icarus Verilog (iverilog)

include $(COCOTB)/share/makefiles/Makefile.sim
