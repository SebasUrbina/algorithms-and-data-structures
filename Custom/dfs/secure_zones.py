"""
🧩 Problema: "Contar zonas seguras"
🔹 Dificultad: Fácil-Media
🔹 Categoría: DFS en matriz (grid traversal)
🔹 Tema: Flood fill / Componentes conectados

📝 Enunciado
Dado un mapa representado por una matriz grid de m x n, donde:

'S' representa una zona segura,

'X' representa una zona peligrosa (no se puede pasar),

Cuenta cuántas zonas seguras conectadas existen en el mapa.
Dos celdas seguras están conectadas si están adyacentes horizontal o verticalmente.
"""

grid = [
    ['S', 'S', 'X', 'X'],
    ['X', 'S', 'X', 'S'],
    ['S', 'X', 'S', 'S'],
    ['X', 'X', 'X', 'S']
]

"""
La solución consiste en hacer un dfs en cada posición 'S' y marcar todos
los vecinos 'S' como visitados. De esta forma cada vez que se inicie un DFs
se hará de una zona segura.
"""
def count_safe_zones(grid):
    
    rows, cols = len(grid), len(grid[0])
    visited = set()

    # Buscamos todos los vecinos que no son S para marcarlos como visitados
    def dfs(r, c): 
        if (
            (r,c) in visited 
            or r<0 or r>=rows 
            or c<0 or c>=cols 
            or grid[r][c] != 'S'
        ):
            return
        visited.add((r,c))

        # Revisamos los vecinos
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # Recorremos toda la grilla
    count = 0
    for r in range(rows):
        for c in range(cols):
            # Si la celda es 'S' y no ha sido visita
            # Recorremos los vecinos que no son 'S' (son 'X')
            # Y los marcamos como visitados
            # Marcamos la zona como segura
            if grid[r][c] == 'S' and (r,c) not in visited:
                dfs(r,c)
                count += 1
    return count


grid = [
    ['S', 'S', 'X', 'X'],
    ['X', 'S', 'X', 'S'],
    ['S', 'X', 'S', 'S'],
    ['X', 'X', 'X', 'S']
]

assert count_safe_zones(grid) == 3, "Error validacion"
print(count_safe_zones(grid))  # Output esperado: 3
            


