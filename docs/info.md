## Cómo funciona

Comparador binario de 4 bits combinacional. Recibe dos números de 4 bits,
A y B, a través del bus de entrada: A en los bits bajos `ui[3:0]` y B en
los bits altos `ui[7:4]`. Compara ambos valores y activa exactamente una
de tres salidas según el resultado: menor, igual o mayor.

Al ser combinacional, no depende del reloj ni del reset — la salida se
actualiza instantáneamente cada vez que cambian las entradas.

## Cómo probarlo

1. Colocar el valor de A en `ui[3:0]` y el valor de B en `ui[7:4]`.
2. Observar las salidas:
   - `uo[0]` se activa cuando A es menor que B.
   - `uo[1]` se activa cuando A es igual a B.
   - `uo[2]` se activa cuando A es mayor que B.
3. Ejemplos de prueba:

| A | B | uo[0] A<B | uo[1] A==B | uo[2] A>B |
|---|---|-----------|------------|-----------|
| 3 | 7 |     1     |     0      |     0     |
| 5 | 5 |     0     |     1      |     0     |
| 9 | 2 |     0     |     0      |     1     |

Solo una salida estará activa a la vez. Las salidas `uo[7:3]` siempre
permanecen en 0.

## Hardware externo

No se requiere hardware externo. Para visualizar los resultados se pueden
conectar 3 LEDs directamente en `uo[0]`, `uo[1]` y `uo[2]` para indicar
visualmente el resultado de la comparación.
