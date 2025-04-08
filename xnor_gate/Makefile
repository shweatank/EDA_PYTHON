# Locate Cocotb
COCOTB := $(shell python3 -c 'import cocotb; print(cocotb.__path__[0])')

# Verilog Source File
VERILOG_SOURCES = xnor_gate.v
TOPLEVEL = xnor_gate
MODULE = test_xnor
SIM = icarus  # Using Icarus Verilog (iverilog)

include $(COCOTB)/share/makefiles/Makefile.sim
