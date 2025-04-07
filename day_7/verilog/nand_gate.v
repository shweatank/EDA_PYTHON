module nand_gate(
    input wire A,
    input wire B,
    output wire Y
);
    assign Y = ~(A & B);

    initial begin
        $dumpfile("nand_gate.vcd");
        $dumpvars(0, nand_gate);
    end
endmodule