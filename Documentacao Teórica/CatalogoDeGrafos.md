# 📊 Catálogo de Grafos com `networkx`

## 1. Grafos Teóricos Clássicos

| Função                  | Descrição                             | Exemplo                     |
|-------------------------|---------------------------------------|-----------------------------|
| `nx.petersen_graph()`   | Grafo de Petersen (3-regular, 10 nós) | `G = nx.petersen_graph()`   |
| `nx.complete_graph(n)`  | Grafo completo com n nós              | `G = nx.complete_graph(5)`  |
| `nx.cycle_graph(n)`     | Grafo cíclico com n nós               | `G = nx.cycle_graph(6)`     |
| `nx.wheel_graph(n)`     | Grafo em forma de roda                | `G = nx.wheel_graph(7)`     |
| `nx.grid_2d_graph(m,n)` | Grafo grade m×n                       | `G = nx.grid_2d_graph(3,3)` |

## 2. Grafos Aleatórios

| Função                           | Descrição                 | Parâmetros                 | Exemplo                                 |
|----------------------------------|---------------------------|----------------------------|-----------------------------------------|
| `nx.erdos_renyi_graph(n, p)`     | Modelo Erdős-Rényi        | `n=nós`, `p=prob. aresta`  | `G = nx.erdos_renyi_graph(15, 0.3)`     |
| `nx.random_regular_graph(d, n)`  | Grafo d-regular aleatório | `d=grau`, `n=nós`          | `G = nx.random_regular_graph(3, 12)`    |
| `nx.watts_strogatz_graph(n,k,p)` | Modelo Pequeno Mundo      | `k=vizinhos`, `p=rewire`   | `G = nx.watts_strogatz_graph(20,4,0.2)` |
| `nx.barabasi_albert_graph(n,m)`  | Modelo Scale-Free         | `n=nós`, `m=arestas novas` | `G = nx.barabasi_albert_graph(50,2)`    |

## 3. Grafos Especiais

| Função                   | Descrição                                  | Exemplo                      |
|--------------------------|--------------------------------------------|------------------------------|
| `nx.mycielski_graph(k)`  | Grafo triangle-free com número cromático k | `G = nx.mycielski_graph(4)`  |
| `nx.sierpinski_graph(k)` | Fractal de Sierpinski                      | `G = nx.sierpinski_graph(4)` |
| `nx.flower_graph(m,n)`   | Grafo flor com m petais                    | `G = nx.flower_graph(3,5)`   |

## 4. Grafos Reais

| Função                            | Descrição                          | Nós | Arestas |
|-----------------------------------|------------------------------------|-----|---------|
| `nx.karate_club_graph()`          | Rede social de clube de karatê     | 34  | 78      |
| `nx.davis_southern_women_graph()` | Rede de relações sociais (1940)    | 32  | 89      |
| `nx.florentine_families_graph()`  | Casamentos entre famílias (Renas.) | 15  | 20      |

## 5. Grafos Direcionados

| Função                                | Descrição                      | Exemplo                                       |
|---------------------------------------|--------------------------------|-----------------------------------------------|
| `nx.directed_havel_hakimi_graph(seq)` | Grafo direcionado Havel-Hakimi | `G = nx.directed_havel_hakimi_graph([3,2,1])` |
| `nx.random_k_out_graph(n,k,alpha)`    | Grafo k-out aleatório          | `G = nx.random_k_out_graph(10,3,0.5)`         |
