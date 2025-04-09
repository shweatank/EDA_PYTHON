TOPLEVEL_LANG = verilog
SIM ?= icarus
VERILOG_SOURCES = i2c.v  # Your Verilog file
TOPLEVEL = i2c_master  # Must match module name in Verilog
MODULE = i2c_ml_test  # Must match Python test filename (without .py)

# --- Optional Settings ---
export WAVES=1  # Enable waveform dumping
COMPILE_ARGS += -g2012 -Wall  # Verilog compilation flags (for iverilog only)

# --- Include cocotb's make rules ---
include $(shell cocotb-config --makefiles)/Makefile.sim