import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # A < B: 3 < 7
    dut.ui_in.value = (7 << 4) | 3   # B=7, A=3
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value & 0b111 == 0b001, "Fallo: A < B"
    dut._log.info("A < B: OK")

    # A == B: 5 == 5
    dut.ui_in.value = (5 << 4) | 5   # B=5, A=5
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value & 0b111 == 0b010, "Fallo: A == B"
    dut._log.info("A == B: OK")

    # A > B: 9 > 2
    dut.ui_in.value = (2 << 4) | 9   # B=2, A=9
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value & 0b111 == 0b100, "Fallo: A > B"
    dut._log.info("A > B: OK")

    dut._log.info("Todos los tests pasaron")
