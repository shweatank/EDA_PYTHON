module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/i2c_master            .fst");
    $dumpvars(0, i2c_master            );
end
endmodule
