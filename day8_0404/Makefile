# Default gate (can be overridden by command line)
GATE ?= nand_gate
TOPLEVEL_LANG = verilog
SIM = icarus
VCD = 1

VERILOG_SOURCES = $(PWD)/$(GATE).v
TOPLEVEL = $(GATE)
MODULE = test_gate  # Python testbench name without .py
SIM_BUILD ?= sim_build/$(GATE)

include $(shell cocotb-config --makefiles)/Makefile.sim
