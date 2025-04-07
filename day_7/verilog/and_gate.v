module and_gate(
    input wire A,
    input wire B,
    output wire Y
);
    assign Y = A & B;

    initial begin
        $dumpfile("and_gate.vcd");
        $dumpvars(0, and_gate);
    end
endmodule