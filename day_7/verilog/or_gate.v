module or_gate(
    input wire A,
    input wire B,
    output wire Y
);
    assign Y = A | B;

    initial begin
        $dumpfile("or_gate.vcd");
        $dumpvars(0, or_gate);
    end
endmodule