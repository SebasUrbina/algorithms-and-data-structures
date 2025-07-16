"""
Depth-First Search (DFS)

DFS es un algoritmo que explora un grafo o arbol profundamente antes de
retroceder.

En lugar de visitar todos los vecinos primero(BFS), DFS va tan profundo como
puede por un camino antes de retroceder

Imagina un laberinto:
Si sigues siempre el camino de la izquierda hasta que no puedas avanzar más,
luego retrocedes y pruebas otro camino
"""

"""
DFS en Grafos
"""

graph = {
    "A": ["B", "C"], 
    "B": ["D"], 
    "C": ["E"], 
    "D": [], 
    "E": ["B"]}


def dfs(graph, node, visited=set()):
    """Implementación recursiva dfs grafos"""
    if node in visited:
        return None
    print(node)
    visited.add(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


dfs(graph, "A")


def dfs(start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()  # Comenzamos con el primer nodo (desde start)
        if node not in visited:  # Si el nodo no ha sido visitado
            print(node)
            visited.add(node)  # Lo agregamos a lo visitados
            for neighbor in reversed(graph[node]):  # Recorremos sus vecinos
                # Reversed hace que se recorra de izquierda a derecha
                stack.append(neighbor)


# Implementación con adj_list

adj_list = [[1, 2], [0, 3], [0], [1], [], [6], [6]]

n = len(adj_list)
visited = [False] * n  # [False,...,False]


# Lo primero que hacemos en dfs es visitar los vecinos de cada nodo
# Para un nodo i visitamos sus vecinos
def dfs(u):
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs(v)


componentes = 0
for i in range(n):
    if not visited[i]:
        dfs(i)  # Recorremos todas las componentes del nodo i.
        componentes += 1
