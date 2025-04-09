TOPLEVEL_LANG = verilog
SIM ?= icarus

# Point to your synthesized netlist
VERILOG_SOURCES = i2c_master_synth.json # Your synthesized netlist file
TOPLEVEL = i2c_master            # Must match module name in netlist
MODULE = test_netlist                # Your Python test file

# Waveform generation
export WAVES=1
export COCOTB_ANSI_OUTPUT=1

include $(shell cocotb-config --makefiles)/Makefile.sim