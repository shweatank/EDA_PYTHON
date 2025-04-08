module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/spi_master.fst");
    $dumpvars(0, spi_master);
end
endmodule
