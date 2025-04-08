module spi_master (
    input clk,
    input start,
    input [7:0] data_in,
    output reg sclk,
    output reg mosi,
    output reg done
);

    reg [7:0] shift_reg;
    reg [2:0] bit_cnt = 0;
    reg busy = 0;

    // VCD dump
    initial begin
        $dumpfile("spi_master.vcd");
        $dumpvars(0, spi_master);
    end

    always @(posedge clk) begin
        if (start && !busy) begin
            busy <= 1;
            shift_reg <= data_in;
            bit_cnt <= 7;
            sclk <= 0;
            done <= 0;
        end else if (busy) begin
            mosi <= shift_reg[bit_cnt];
            sclk <= ~sclk;

            if (sclk) begin
                if (bit_cnt == 0) begin
                    busy <= 0;
                    done <= 1;
                end else begin
                    bit_cnt <= bit_cnt - 1;
                end
            end
        end
    end
endmodule
