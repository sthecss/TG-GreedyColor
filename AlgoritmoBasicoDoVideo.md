# 📊 Algoritmo Básico do Vídeo

```python

import networkx as nx

# 1. Criando um grafo G:
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),  # quadrado
    (0, 2)  # diagonal
])
# Se fosse unidirecional: G.add_edge(u, v)

# 2. Adotar a estratégia:
estrategia = 'saturation_largest_first'

# 3. Dada a estratégia, aplicar a coloração
coloracao = nx.coloring.greedy_color(G, strategy=estrategia)

# Retornos no terminal:
num_cores = max(coloracao.values()) + 1

print(f"{'-'*50} GRÁFICO:")
print(f"{'- Nós:':<25} {G.number_of_nodes()}")
print(f"{'- Arestas:':<25} {G.number_of_edges()}")
print(f"{'- Conexo:':<25} {'Sim' if nx.is_connected(G) else 'Não'}")
print(f"{'- Coloração dos nós:':<25} {coloracao}")
print(f"{'- Cores:':<25} {num_cores}")


```
