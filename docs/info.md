<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Contador binario de 4 bits sincrónico. Incrementa su valor en cada flanco positivo del reloj cuando la señal de habilitación (`en`) está activa. El contador cuenta de 0 a 15 (0000 a 1111 en binario) y regresa automáticamente a 0 al desbordar. La señal `carry` se activa cuando el contador está en 15 y está habilitado, indicando que en el siguiente ciclo de reloj ocurrirá un desbordamiento.

El reset es asíncrono y activo en bajo (`rst_n`): al poner esta señal en 0, el contador regresa inmediatamente a 0 sin importar el estado del reloj.

## How to test

1. Mantener `rst_n` en bajo para inicializar el contador en 0.
2. Liberar `rst_n` (ponerlo en alto).
3. Activar `ui[0]` (enable) en alto.
4. Aplicar pulsos de reloj y observar cómo `uo[3:0]` incrementa
   de 0000 a 1111.
5. Verificar que `uo[4]` (carry) se activa cuando el contador llega a 15.
6. Para pausar el conteo, poner `ui[0]` en bajo: el valor se congela.
7. Para reiniciar en cualquier momento, poner `rst_n` en bajo.

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
