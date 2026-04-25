/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */
`default_nettype none

module tt_um_comparador_4bit (
    input  wire [7:0] ui_in,    // ui_in[3:0] = A,  ui_in[7:4] = B
    output wire [7:0] uo_out,   // uo_out[0] = A<B, uo_out[1] = A==B, uo_out[2] = A>B
    input  wire [7:0] uio_in,   // no utilizado
    output wire [7:0] uio_out,  // no utilizado
    output wire [7:0] uio_oe,   // no utilizado
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire [3:0] A;
    wire [3:0] B;

    assign A = ui_in[3:0];
    assign B = ui_in[7:4];

    assign uo_out[0] = (A < B);   // menor
    assign uo_out[1] = (A == B);  // igual
    assign uo_out[2] = (A > B);   // mayor
    assign uo_out[7:3] = 5'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
