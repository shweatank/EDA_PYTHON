module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/nor_gate.fst");
    $dumpvars(0, nor_gate);
end
endmodule
