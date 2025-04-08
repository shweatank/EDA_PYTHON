module uart_tx (
    input clk,
    input start,
    input [7:0] data,
    output reg tx = 1,
    output reg done
);

    // Parameter to divide clock frequency for baud rate timing
    parameter BAUD_DIV = 10;    // Controls the baud rate. Assumes clk is 10x faster than baud.

    reg [3:0] bit_cnt;
    reg [9:0] shift_reg;
    reg [3:0] baud_cnt;
    reg busy = 0;
    // Sequential logic triggered on the rising edge of the clock
    always @(posedge clk) begin
        // If 'start' signal is high and not currently transmitting
        if (start && !busy) begin
            // Load shift register: [stop bit (1), data (8 bits), start bit (0)]
            shift_reg <= {1'b1, data, 1'b0};
            bit_cnt <= 9;
            baud_cnt <= 0;
            busy <= 1;
            done <= 0;
        end

        else if (busy) begin
            if (baud_cnt == BAUD_DIV - 1) begin

                tx <= shift_reg[0];
                // Right shift to bring next bit to LSB
                shift_reg <= shift_reg >> 1;
                baud_cnt <= 0;

                if (bit_cnt == 0) begin
                    busy <= 0;
                    done <= 1;
                end else begin
                    bit_cnt <= bit_cnt - 1;
                end
            end else begin
                baud_cnt <= baud_cnt + 1;
            end
        end
    end

    // VCD waveform dump for simulation (Cocotb or other tools)
    initial begin
        $dumpfile("results/wave.vcd");
        $dumpvars(0, uart_tx);
    end

endmodule
