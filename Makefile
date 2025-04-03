
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = nand_gate.v
TOPLEVEL = nand_gate
MODULE = test_nand
export WAVES=1
include $(shell cocotb-config --makefiles)/Makefile.sim
