module nor_gate(
    input wire A,
    input wire B,
    output wire Y
);
    assign Y = ~(A | B);

    initial begin
        $dumpfile("nor_gate.vcd");
        $dumpvars(0, nor_gate);
    end
endmodule