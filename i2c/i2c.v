module i2c_master (
    input clk,
    input start,
    input [6:0] addr,
    input [7:0] data,
    output reg scl = 1,  // Default high (idle)
    output reg sda = 1   // Default high (idle)
);
    reg [3:0] bit_cnt;
    reg [15:0] shift_reg;
    reg busy = 0;

    always @(posedge clk) begin
        if (start && !busy) begin
            busy <= 1;
            shift_reg <= {addr, 1'b0, data};  // Write bit = 0
            bit_cnt <= 15;
            scl <= 0;  // Start condition
            sda <= 0;
        end 
        else if (busy) begin
            scl <= ~scl;  // Toggle clock
            if (scl) begin
                sda <= shift_reg[bit_cnt];
                bit_cnt <= bit_cnt - 1;
            end
            if (bit_cnt == 0) busy <= 0;
        end
    end

    initial begin
        $dumpfile("i2c.vcd");
        $dumpvars(0, i2c_master);
    end
endmodule