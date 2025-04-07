module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/not_gate.fst");
    $dumpvars(0, not_gate);
end
endmodule
