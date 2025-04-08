module xnor_gate (
    input wire A,
    input wire B,
    output wire Y
);
    assign Y = ~(A ^ B); // XNOR logic

    initial begin
        $dumpfile("xnor_gate.vcd");
        $dumpvars(0, xnor_gate);
    end
endmodule
