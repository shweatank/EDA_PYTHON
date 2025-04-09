`timescale 1ns/1ps

module i2c_master_tb;

    reg clk = 0;
    reg start = 0;
    reg [6:0] addr = 7'b1010000;  // example slave address
    reg [7:0] data = 8'h5A;       // example data
    wire scl;
    wire sda;

    // Instantiate the I2C Master
    i2c_master uut (
        .clk(clk),
        .start(start),
        .addr(addr),
        .data(data),
        .scl(scl),
        .sda(sda)
    );

    // Clock generator
    always #5 clk = ~clk;

    initial begin
        // Dump VCD
        $dumpfile("i2c_master.vcd");
        $dumpvars(0, i2c_master_tb);

        // Wait for a few cycles
        #20;
        start = 1;    // Trigger I2C start condition
        #10;
        start = 0;    // Release start

        // Wait for transaction to complete
        #500;

        $finish;
    end
endmodule
