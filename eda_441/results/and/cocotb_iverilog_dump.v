module cocotb_iverilog_dump();
initial begin
    $dumpfile("results/and/and.fst");
    $dumpvars(0, and);
end
endmodule
