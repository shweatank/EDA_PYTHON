module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/alu/alu.fst");
    $dumpvars(0, alu);
end
endmodule
