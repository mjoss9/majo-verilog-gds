/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */
`default_nettype none

module tt_um_counter_4bit (
    input  wire [7:0] ui_in,    // Dedicated inputs  - ui_in[0] = en
    output wire [7:0] uo_out,   // Dedicated outputs - uo_out[3:0] = count, uo_out[4] = carry
    input  wire [7:0] uio_in,   // IOs: Input path   - no utilizado
    output wire [7:0] uio_out,  // IOs: Output path  - no utilizado
    output wire [7:0] uio_oe,   // IOs: Enable path  - no utilizado
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    wire        en;
    reg  [3:0]  count;
    wire        carry;

    assign en    = ui_in[0];
    assign carry = (count == 4'hF) & en;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 4'b0000;
        else if (en)
            count <= count + 1'b1;
    end

    // Asignar salidas
    assign uo_out  = {3'b000, carry, count};  // [4]=carry, [3:0]=count
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Entradas no utilizadas
    wire _unused = &{ena, uio_in, ui_in[7:1], 1'b0};

endmodule
