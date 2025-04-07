module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/xor_gate/xor_gate.fst");
    $dumpvars(0, xor_gate);
end
endmodule
