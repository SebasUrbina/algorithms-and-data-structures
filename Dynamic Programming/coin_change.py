"""
# Coin Change Problem

Dado un conjunto de monedas de denominaciones coins[] y una cantidad amount, 
encuentra el número mínimo de monedas que necesitas para alcanzar amount. 
Si no puedes alcanzar la cantidad exacta, devuelve -1.

### Ejemplo

Coins: [1,2,5], amount = 11
Output: 3 (5+5+1)

1. El objetivo es encontrar la cantidad mínima de monedas necesarias para alcanzar amount. 
El subproblema consiste en encontrar el mínimo número de monedas necesarias para alcanzar una cantidad i, siendo i cualquier número entre 0 y amount.

2. Para cada i (donde i es la cantidad), 

dp[0] = 0
dp[i] = min(dp[i-coin_j] + 1) 
"""
from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    # Array de longitud amount + 1 donde cada posicion por defecto es infinito
    # ya que queremos minimizar el número de monedas y aún no sabemos.
    dp = [float("inf")] * (amount + 1)

    # Caso base, para alcanzar 0 no necesitamos ninguna moneda.
    dp[0] = 0

    for i in range(1, amount+1):   
        # Para cada moneda actualizamos el valor de dp[i]
        for coin in coins:
            if i - coin >=0: # Verificamos que podemos usar la moneda. 
                # Actualizamos dp[i] como el minimo entre su valor actual
                # y dp[i-coin], es decir, el numero de monedas necesarias
                # para formar i-coin + 1 moneda.
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Si dp[amount] sigue siendo infinito, no es posible formar esa cantidad
    return dp[amount] if dp[amount] != float("inf") else -1

    
# Example
coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))