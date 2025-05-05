# 📍 Índice 
| Sobre | Acesso |
|--------|----------|
| Explicação da função `greedy_color` | [nx.coloring.greedy_color](#-nxcoloringgreedy_colorg-strategyestrategia)  |
| Explicação da função `visualizar_grafo` | [visualizar_grafo(grafo, nome_grafo, estrategia, coloracao)](#-visualizar_grafografo-nome_grafo-estrategia-coloracao)  |

---

# 📚 `nx.coloring.greedy_color(G, strategy=estrategia)`

## 1. O que é?
[🔝 Voltar ao índice](#-índice)

A função `greedy_color()` do pacote `networkx` realiza uma **coloração gulosa de vértices** em um grafo. O objetivo é **atribuir cores (valores inteiros)** aos nós do grafo de modo que **nenhum par de vértices adjacentes tenha a mesma cor** — ou seja, uma **coloração própria**.

Ela retorna um **dicionário**, onde as chaves são os nós e os valores são as cores atribuídas:

```python
{nó_1: cor_1, nó_2: cor_2, ..., nó_n: cor_n}
```

---

## 2. Sintaxe
[🔝 Voltar ao índice](#-índice)

```python
nx.coloring.greedy_color(G, strategy='nome_da_estrategia')
```

- `G`: grafo a ser colorido (do tipo `nx.Graph`)
- `strategy`: string que define a estratégia de ordenação dos nós

---

## 3. Como funciona?
[🔝 Voltar ao índice](#-índice)

O algoritmo percorre os nós do grafo em uma **ordem definida pela estratégia**, e para cada nó:

1. Verifica as cores já usadas por seus vizinhos.
2. Atribui a **menor cor disponível** que não conflita com seus vizinhos.
3. Passa para o próximo nó.

> É chamado "guloso" porque toma decisões locais que parecem boas no momento, sem olhar o futuro.

---

## 4. Principais Estratégias
[🔝 Voltar ao índice](#-índice)

| Estratégia                       | Descrição                                                                 |
|----------------------------------|---------------------------------------------------------------------------|
| `'largest_first'`               | Começa pelos nós com maior grau (mais vizinhos).                          |
| `'random_sequential'`           | Ordem aleatória.                                                          |
| `'smallest_last'`               | Ordena os nós do menor para o maior grau final.                          |
| `'saturation_largest_first'`    | **DSATUR**: escolhe o nó com maior saturação (mais vizinhos com cores diferentes). |
| `'independent_set'`             | Usa conjuntos independentes.                                             |
| `'connected_sequential_bfs'`    | Ordem baseada em busca em largura (BFS).                                 |
| `'connected_sequential_dfs'`    | Ordem baseada em busca em profundidade (DFS).                            |

---

# 📚 `visualizar_grafo(grafo, nome_grafo, estrategia, coloracao)`
[🔝 Voltar ao índice](#-índice)

## 📑 Índice

1. [Criação da figura com tamanho personalizado](#1-criação-da-figura-com-tamanho-personalizado)  
2. [Cálculo das posições dos nós com spring layout](#2-cálculo-das-posições-dos-nós-com-spring-layout)  
3. [Criação da barra de cores (colorbar)](#3-criação-da-barra-de-cores-colorbar)  
4. [Desenho dos nós com cores baseadas na coloração](#4-desenho-dos-nós-com-cores-baseadas-na-coloração)  
5. [Desenho das arestas do grafo](#5-desenho-das-arestas-do-grafo)  
6. [Adição de rótulos aos nós](#6-adição-de-rótulos-aos-nós)  
7. [Adição de título com informações do grafo](#7-adição-de-título-com-informações-do-grafo)  
8. [Ajustes finais na visualização](#8-ajustes-finais-na-visualização)

---

## 1. Criação da figura com tamanho personalizado
[🔝 Voltar ao índice](#-índice)
```python
plt.figure(figsize=(20, 15))
````

Cria uma figura do matplotlib com largura 20 e altura 15. Isso garante que o grafo não fique apertado e todos os nós fiquem visíveis, mesmo em grafos grandes.

---

## 2. Cálculo das posições dos nós com spring layout
[🔝 Voltar ao índice](#-índice)
```python
pos = nx.spring_layout(grafo, seed=42, k=3.5, iterations=600)
```

* `spring_layout`: posiciona os nós com base em forças de atração/repulsão simuladas (como se fossem ímãs).
* `seed=42`: garante que o layout seja sempre igual ao rodar várias vezes.
* `k=3.5`: define a distância ideal entre os nós.
* `iterations=600`: número de vezes que a simulação roda para estabilizar as posições.

---

## 3. Criação da barra de cores (colorbar)
[🔝 Voltar ao índice](#-índice)
```python
cbar = plt.colorbar(
    plt.cm.ScalarMappable(
        cmap=plt.cm.tab20,
        norm=plt.Normalize(vmin=0, vmax=max(coloracao.values()))
    ),
    ax=plt.gca()
)
cbar.set_ticks(range(len(set(coloracao.values()))))
```

* `plt.cm.tab20`: define uma paleta de até 20 cores distintas.
* `Normalize`: mapeia os valores de coloração para as cores.
* `colorbar`: adiciona uma barra de referência que mostra o que cada cor representa.

---

## 4. Desenho dos nós com cores baseadas na coloração
[🔝 Voltar ao índice](#-índice)
```python
nx.draw_networkx_nodes(
    grafo, pos,
    node_color=[coloracao[n] for n in grafo.nodes()],
    cmap=plt.cm.tab20,
    node_size=600,
    edgecolors='black'
)
```

* `node_color`: define a cor de cada nó, baseada no dicionário `coloracao`.
* `cmap`: mesmo mapa de cores usado na colorbar.
* `node_size=600`: define o tamanho dos nós.
* `edgecolors='black'`: contorno preto ao redor dos nós.

---

## 5. Desenho das arestas do grafo
[🔝 Voltar ao índice](#-índice)
```python
nx.draw_networkx_edges(
    grafo, pos,
    width=1.0,
    alpha=0.4,
    edge_color='gray'
)
```

* `width=1.0`: define a espessura das linhas.
* `alpha=0.4`: deixa as linhas parcialmente transparentes.
* `edge_color='gray'`: cor das arestas (linhas entre os nós).

---

## 6. Adição de rótulos aos nós
[🔝 Voltar ao índice](#-índice)
```python
labels = {n: str(n) for n in grafo.nodes()}
nx.draw_networkx_labels(
    grafo, pos,
    labels=labels,
    font_size=6,
)
```

* Cria um dicionário `labels` com os nomes dos nós.
* `font_size=6`: tamanho da fonte para manter legível mesmo com muitos nós.

---

## 7. Adição de título com informações do grafo
[🔝 Voltar ao índice](#-índice)
```python
plt.title(
    f"Grafo: {nome_grafo}\n"
    f"Estratégia: {estrategia.upper()} | "
    f"Cores usadas: {max(coloracao.values()) + 1}\n"
    f"Nós: {grafo.number_of_nodes()} | Arestas: {grafo.number_of_edges()}"
)
```

Adiciona um título com:

* Nome do grafo (`nome_grafo`)
* Estratégia de coloração (`estrategia`)
* Número de cores utilizadas
* Quantidade de nós e arestas no grafo

---

## 8. Ajustes finais na visualização
[🔝 Voltar ao índice](#-índice)
```python
plt.axis('off')
plt.tight_layout()
plt.show()
```

* `axis('off')`: remove os eixos do gráfico para visualização limpa.
* `tight_layout()`: organiza tudo para que nada fique cortado.
* `show()`: exibe o grafo finalizado.

---

