# Dynamic programming problems

## 1. [Coin Change Problem]((https://chatgpt.com/share/ee3ce1ec-e51f-4fce-93f4-956aedc6f1c2))
Tienes monedas de diferentes valores y una cantidad de dinero. Tu objetivo es encontrar el número mínimo de monedas necesarias para alcanzar exactamente esa cantidad. Si no es posible, debes devolver `-1`.

### Ejemplo
- **Monedas**: `[1, 2, 5]`
- **Cantidad**: `11`
- **Salida esperada**: `3` (porque `11 = 5 + 5 + 1`)

## Enfoque Paso a Paso

### 1. Crear una tabla para guardar soluciones parciales (dp array)
Imagina que tienes una tabla (o lista) llamada `dp[]` donde cada posición te dice el número mínimo de monedas que necesitas para formar una cantidad.

- `dp[i]` = El número mínimo de monedas para formar la cantidad `i`.

Al principio, no sabemos cuántas monedas necesitamos para cada cantidad, así que llenamos la tabla con valores "muy grandes" (como infinito) para indicar que no sabemos aún.

Excepto `dp[0] = 0`, porque no necesitamos ninguna moneda para formar la cantidad 0.

**Ejemplo inicial:**
Si la cantidad que queremos formar es 11, la tabla al principio se vería así:
```python
dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
```
Donde cada posición representa una cantidad. La posición dp[0] es 0 porque no necesitas monedas para hacer 0, y las demás son inf porque no sabemos cuántas monedas necesitamos para esas cantidades aún.

### 2. Recorrer cada cantidad desde 1 hasta ``amount`` (en este caso, 11)

Ahora queremos rellenar la tabla desde ``dp[1]`` hasta ``dp[amount]`` (es decir, hasta dp[11]). Para cada cantidad i, probamos todas las monedas disponibles (1, 2, 5), y vemos si usar esa moneda nos lleva a una solución mejor.

### 3. Probar cada moneda para cada cantidad

Para cada cantidad i, vamos a tratar de usar cada una de las monedas que tenemos (1, 2, 5). Si usar la moneda me ayuda a formar la cantidad, actualizo ``dp[i]``.

Ejemplo: ``i = 1``
- Si quiero formar la cantidad 1, puedo usar la moneda de 1. La cantidad restante sería 1 - 1 = 0. Ya sabemos que ``dp[0] = 0`` (no necesitamos monedas para formar 0), así que necesitamos una moneda más para formar 1. Entonces:
    ```python
    dp[1] = dp[0] + 1 = 1
    ```
    Ahora la tabla dp[] se vería así:
    ```python
    dp = [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
    ```

Ejemplo: ``i = 2``
- Si quiero formar 2, puedo usar la moneda de 1. Me quedaría formar 2 - 1 = 1, y ya sé que ``dp[1] = 1`` (necesito 1 moneda para formar 1). Entonces necesito 1 moneda más para formar 2:
    ```python
    dp[2] = dp[1] + 1 = 2
    ```
    También puedo usar la moneda de 2. Me quedaría formar 2 - 2 = 0, y ya sé que dp[0] = 0. Solo necesito una moneda:
    ```python
    dp[2] = dp[0] + 1 = 1
    ```

Ahora ``dp[2]`` se actualiza a 1 (porque es mejor usar una moneda de 2 que dos monedas de 1).

La tabla ``dp[]`` se vería así:
```python
dp = [0, 1, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf]
```

Ejemplo: ``i = 3``
- Si quiero formar 3, puedo usar la moneda de 1. Me quedaría formar 3 - 1 = 2, y ya sé que dp[2] = 1. Entonces, necesito 1 moneda más:
    ```python
    dp[3] = dp[2] + 1 = 2
    ```
    También puedo usar la moneda de 2. Me quedaría formar 2 - 2 = 0, y ya sé que ``dp[0] = 0``. Solo necesito una moneda:
    ```python
    dp[2] = dp[0] + 1 = 1
    ```
La tabla ``dp[]`` ahora:
```python
dp = [0, 1, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf]
```
