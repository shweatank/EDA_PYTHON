module i2c_master (
    input clk,
    input start,
    input [6:0] addr,
    input [7:0] data,
    output reg scl = 0,   // Initialize scl
    output reg sda = 1    // Initialize sda (optional, often idle high)
);

    reg [3:0] bit_cnt = 0;
    reg [15:0] shift_reg;
    reg busy = 0;

    always @(posedge clk) begin
        if (start && !busy) begin
            busy <= 1;
            shift_reg <= {addr, 1'b0, data}; // Write bit = 0
            bit_cnt <= 15;
            scl <= 0;  // start from low
        end else if (busy) begin
            scl <= ~scl; // toggle clock
            if (scl) begin
                sda <= shift_reg[bit_cnt];
                bit_cnt <= bit_cnt - 1;
            end
            if (bit_cnt == 0) begin
                busy <= 0;
                scl <= 0;
            end
        end
    end
endmodule
