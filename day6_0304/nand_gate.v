module nand_gate(
    input wire A,
    input wire B,
    output wire Y
);

    assign Y = ~(A & B);

    initial begin
        $dumpfile("dump.vcd");  // Set VCD filename
        $dumpvars(0, nand_gate); // Dump all variables
    end
endmodule
