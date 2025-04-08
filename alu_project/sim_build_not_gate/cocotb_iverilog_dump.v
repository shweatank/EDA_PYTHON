module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build_not_gate/not_gate.fst");
    $dumpvars(0, not_gate);
end
endmodule
