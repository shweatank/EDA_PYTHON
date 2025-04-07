module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/nor_gate/nor_gate.fst");
    $dumpvars(0, nor_gate);
end
endmodule
