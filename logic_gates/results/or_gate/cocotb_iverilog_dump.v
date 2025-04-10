module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/or_gate/or_gate.fst");
    $dumpvars(0, or_gate);
end
endmodule
