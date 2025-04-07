`timescale 1ns/1ps
module tb_adder;

    reg [3:0] a, b;
    wire [4:0] sum;

    adder uut (
        .a(a),
        .b(b),
        .sum(sum)
    );

    initial begin
        $dumpfile("wave.vcd"); // Output waveform file
        $dumpvars(0, tb_adder); // Dump all signals recursively

        a = 4'b0000; b = 4'b0000;
        #10 a = 4'b0011; b = 4'b0101; // 3 + 5 = 8
        #10 a = 4'b1111; b = 4'b0001; // 15 + 1 = 16
        #10 a = 4'b1010; b = 4'b1010; // 10 + 10 = 20
        #10 $finish;
    end

endmodule