TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/nor_gate.v
TOPLEVEL = nor_gate
MODULE = test_nor  # Name of the Python test module

SIM = icarus
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim
