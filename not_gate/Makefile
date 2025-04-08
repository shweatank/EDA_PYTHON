# Makefile for NOT gate simulation using Cocotb

TOPLEVEL_LANG = verilog
SIM = icarus
MODULE = test_not_gate       # Name of the Python testbench module (without .py)
TOPLEVEL = not_gate          # Name of the Verilog top module
VERILOG_SOURCES = $(shell pwd)/not_gate.v

# Optional: Set output directory
SIM_BUILD = sim_build

# Run with waveform dump
COMPILE_ARGS = -D DUMP

include $(shell cocotb-config --makefiles)/Makefile.sim
