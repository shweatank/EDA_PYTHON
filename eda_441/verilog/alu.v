module alu (
    input [3:0] A,
    input [3:0] B,
    input [2:0] ALU_Sel,
    output reg [3:0] ALU_Out,
    output reg CarryOut
);

    always @(*) begin
        case (ALU_Sel)
            3'b000: {CarryOut, ALU_Out} = A + B;       // Addition
            3'b001: {CarryOut, ALU_Out} = A - B;       // Subtraction
            3'b010: begin ALU_Out = A & B; CarryOut = 0; end // AND
            3'b011: begin ALU_Out = A | B; CarryOut = 0; end // OR
            3'b100: begin ALU_Out = A ^ B; CarryOut = 0; end // XOR
            3'b101: begin ALU_Out = ~A; CarryOut = 0; end     // NOT
            3'b110: begin ALU_Out = A << 1; CarryOut = 0; end // Shift Left
            3'b111: begin ALU_Out = A >> 1; CarryOut = 0; end // Shift Right
            default: begin ALU_Out = 4'b0000; CarryOut = 0; end
        endcase
    end

    initial begin
        $dumpfile("VCD/alu.vcd");
        $dumpvars(0, alu);
    end

endmodule
