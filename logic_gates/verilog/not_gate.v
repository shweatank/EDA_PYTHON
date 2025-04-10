module not_gate(
    input wire A,
    output wire Y
);
    assign Y = ~A;

    initial begin
        $dumpfile("not_gate.vcd");
        $dumpvars(0, not_gate);
    end
endmodule