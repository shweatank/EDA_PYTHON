module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/not_gate/not_gate.fst");
    $dumpvars(0, not_gate);
end
endmodule
