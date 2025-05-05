# Estratégias de Coloração de Grafos no NetworkX

Este documento descreve em detalhes as principais estratégias de coloração de vértices disponíveis no NetworkX, suas características, complexidade e casos de uso recomendados.

---

## Tabela Resumo

| Estratégia                                  | Descrição                                         | Complexidade | Quando Usar                                  |
|---------------------------------------------|---------------------------------------------------|--------------|----------------------------------------------|
| **`largest_first`**                         | Ordena os vértices por grau decrescente           | O(n log n)   | Grafos com hubs ou nós centrais              |
| **`random_sequential`**                     | Processa os vértices em ordem aleatória           | O(n)         | Testes estatísticos ou aleatoriedade         |
| **`smallest_last`**                         | Remove iterativamente vértices de menor grau      | O(n²)        | Grafos equilibrados ou esparsos              |
| **`independent_set`**                       | Colore por conjuntos independentes máximos        | O(n²)        | Grafos esparsos e grandes                    |
| **`connected_sequential_bfs`**              | Usa BFS para definir a ordem de coloração         | O(n + m)     | Grafos com conectividade local forte         |
| **`connected_sequential_dfs`**              | Usa DFS para definir a ordem de coloração         | O(n + m)     | Grafos com hierarquias ou caminhos profundos |
| **`connected_sequential`**                  | Combina BFS e DFS em componentes conexas          | O(n + m)     | Grafos com múltiplas componentes             |
| **`saturation_largest_first`** (**DSATUR**) | Prioriza nós com maior saturação (cores vizinhas) | O(n²)        | Grafos complexos; ótimo desempenho prático   |
| **`DSATUR`**                                | Alias para `saturation_largest_first`             | O(n²)        | -                                            |

---

## Estratégias em Detalhe

### `largest_first`
Ordena os vértices do maior para o menor grau.
- **Motivação**: Colorir primeiro os nós mais conectados.
- **Vantagem**: Geralmente reduz o número total de cores utilizadas.

---

### `random_sequential`
Escolhe os vértices em ordem aleatória.
- **Vantagem**: Gera diferentes colorações; útil como base para métodos estocásticos.

---

### `smallest_last`
Remove recursivamente os vértices de menor grau, depois colore em ordem inversa.
- **Vantagem**: Tende a minimizar o número de cores em grafos esparsos.

---

### `independent_set`
Agrupa vértices em conjuntos independentes (sem conexões entre si) e colore cada conjunto com uma cor.
- **Vantagem**: Eficiente em grafos grandes e pouco conectados.

---

### `connected_sequential_bfs`
Realiza uma busca em largura (BFS) para definir a ordem de coloração.
- **Uso**: Preserva a conectividade local do grafo.

---

### `connected_sequential_dfs`
Utiliza uma busca em profundidade (DFS) para ordenar os vértices antes de colorir.
- **Diferença**: Pode gerar agrupamentos mais profundos ou sequenciais.

---

### `connected_sequential`
Aplica coloração sequencial por componentes conexas, combinando abordagens BFS e DFS.
- **Uso**: Útil para grafos desconexos ou com subgrupos distintos.

---

### `saturation_largest_first` (ou `DSATUR`)
Em cada passo, escolhe o vértice com maior **saturação** — ou seja, com o maior número de cores distintas em seus vizinhos.
- **Empate**: Resolvido pelo maior grau.
- **Vantagem**: Muito eficaz em minimizar cores em grafos densos ou irregulares.

---

## Observação
Todas essas estratégias são heurísticas. Elas não garantem a coloração ótima (mínimo número de cores), mas funcionam bem na prática para muitos tipos de grafos.

---

## Exemplo em NetworkX

```python
import networkx as nx
from networkx.algorithms.coloring import greedy_color

G = nx.karate_club_graph()
cores = greedy_color(G, strategy="largest_first")
nx.draw(G, node_color=[cores[n] for n in G.nodes()], with_labels=True)
````

---

## Referências

* [NetworkX Documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.coloring.greedy_color.html)
* Welsh, D. J. A., & Powell, M. B. (1967). An upper bound for the chromatic number of a graph and its application to timetabling problems.

```
