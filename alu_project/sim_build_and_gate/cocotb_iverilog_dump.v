module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build_and_gate/and_gate.fst");
    $dumpvars(0, and_gate);
end
endmodule
