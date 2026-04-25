# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0   # en = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Verificar que el contador inicia en 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, f"Esperado 0, obtenido {dut.uo_out.value}"

    # Activar enable y contar
    dut._log.info("Probando conteo")
    dut.ui_in.value = 1   # en = 1

    for i in range(1, 16):
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == i, f"Esperado {i}, obtenido {dut.uo_out.value}"
        dut._log.info(f"count = {i}")

    # Verificar carry en 15
    assert (dut.uo_out.value >> 4) & 1 == 1, "Carry debería estar activo en 15"

    # Verificar rollover a 0
    await ClockCycles(dut.clk, 1)
    assert (dut.uo_out.value & 0xF) == 0, "El contador debería reiniciarse a 0"

    # Probar pausa con enable = 0
    dut._log.info("Probando pausa")
    dut.ui_in.value = 0   # en = 0
    await ClockCycles(dut.clk, 5)
    assert (dut.uo_out.value & 0xF) == 0, "El contador no debería avanzar sin enable"

    dut._log.info("Test completado exitosamente")
