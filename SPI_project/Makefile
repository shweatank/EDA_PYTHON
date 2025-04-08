TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/spi_master.v
TOPLEVEL = spi_master
MODULE = test_spi_master

SIM = icarus
WAVES = 1

IVERILOG_ARGS = -g2012

include $(shell cocotb-config --makefiles)/Makefile.sim
