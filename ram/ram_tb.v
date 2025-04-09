`timescale 1ns/1ps

module ram_tb;
  parameter D_WIDTH = 16;
  parameter A_WIDTH = 5;

  // Signals
  reg clk_write, clk_read;
  reg [A_WIDTH-1:0] address_write, address_read;
  reg [D_WIDTH-1:0] data_write;
  reg write_enable;
  wire [D_WIDTH-1:0] data_read;

  // Instantiate the RAM module
  ram #(D_WIDTH, A_WIDTH) uut (
    .clk_write(clk_write),
    .address_write(address_write),
    .data_write(data_write),
    .write_enable(write_enable),
    .clk_read(clk_read),
    .address_read(address_read),
    .data_read(data_read)
  );

  // Clock generation
  initial begin
    clk_write = 0;
    forever #5 clk_write = ~clk_write;
  end

  initial begin
    clk_read = 0;
    forever #7 clk_read = ~clk_read; // Different clock domain
  end

  // Test sequence
  initial begin
    // VCD setup
    $dumpfile("ram.vcd");
    $dumpvars(0, ram_tb);

    // Initial values
    write_enable = 0;
    address_write = 0;
    data_write = 0;
    address_read = 0;

    // Wait a bit
    #10;

    // Write to address 3
    write_enable = 1;
    address_write = 5'd3;
    data_write = 16'hABCD;
    #10;

    // Write to address 7
    address_write = 5'd7;
    data_write = 16'h1234;
    #10;

    write_enable = 0; // Stop writing

    // Read from address 3
    address_read = 5'd3;
    #15;

    // Read from address 7
    address_read = 5'd7;
    #15;

    // Finish simulation
    $finish;
  end
endmodule
