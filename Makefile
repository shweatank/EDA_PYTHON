COCOTB := $(shell python3 -c 'import cocotb; print(cocotb.__path__[0])')
VERILOG_SOURCES := nand_gate.v
TOPLEVEL := nand_gate
MODULE := test_nand
SIM := icarus
include $(COCOTB)/share/makefiles/Makefile.sim

# pip install cocotb
# pip show cocotb
# sudo apt install iverilog gtkwave
# iverilog -V
# sudo apt install make
# SIM=icarus TOPLEVEL=nand_gate MODULE=test_nand make