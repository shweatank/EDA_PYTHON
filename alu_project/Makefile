TOPLEVEL_LANG = verilog
SIM ?= icarus

VERILOG_SOURCES = verilog/$(GATE).v
TOPLEVEL = $(GATE)
MODULE = test_cases.test_$(GATE)

export WAVES = 1
SIM_BUILD = sim_build_$(GATE)
include $(shell cocotb-config --makefiles)/Makefile.sim
synth_%:
	echo "read_verilog verilog/$*.v" > synth.ys
	echo "hierarchy -check -top $*" >> synth.ys
	echo "proc; opt; fsm; opt" >> synth.ys
	echo "techmap; opt" >> synth.ys
	echo "write_verilog -noattr verilog/netlist_$*.v" >> synth.ys
	yosys synth.ys
netlist_test_%:
	@echo "Simulating netlist version of $*"
	make SIM=icarus MODULE=test_$* TOPLEVEL=$* VERILOG_SOURCES=verilog/netlist_$*.v TOPLEVEL_LANG=verilog
