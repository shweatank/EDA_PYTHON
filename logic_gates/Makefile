# TOPLEVEL_LANG = verilog
# SIM ?= icarus
# VERILOG_SOURCES = verilog/$(GATE).v
# TOPLEVEL = $(GATE)
# MODULE = test_cases.test_$(GATE)
# export WAVES=1
# include $(shell cocotb-config --makefiles)/Makefile.sim

# Results Configuration
RESULTS_DIR ?= results
COCOTB_JSON_CONFIG = $(RESULTS_DIR)/results.json
export PYTHONPATH := $(PWD):$(PYTHONPATH)

# Simulation Configuration
TOPLEVEL_LANG = verilog
SIM ?= icarus
VERILOG_SOURCES = verilog/$(GATE).v
TOPLEVEL = $(GATE)
MODULE = test_cases.test_$(GATE)
export WAVES=1

include $(shell cocotb-config --makefiles)/Makefile.sim