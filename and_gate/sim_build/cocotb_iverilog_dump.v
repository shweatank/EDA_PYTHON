module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/and_gate.fst");
    $dumpvars(0, and_gate);
end
endmodule
