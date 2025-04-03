module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/nand_gate.fst");
    $dumpvars(0, nand_gate);
end
endmodule
