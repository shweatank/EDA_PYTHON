TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/or_gate.v
TOPLEVEL = or_gate
MODULE = test_or  # Name of the Python test module

SIM = icarus
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim
