module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/and_gate/and_gate.fst");
    $dumpvars(0, and_gate);
end
endmodule
