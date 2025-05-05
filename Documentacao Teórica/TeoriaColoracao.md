# Teoria: Coloração de Grafos — Expansão Teórica

## Definição formal

Seja $G = (V, E)$ um grafo simples e não direcionado, uma **coloração própria de vértices** é uma função $f: V \rightarrow C$ tal que:

> Para toda aresta $(u, v) \in E$, temos $f(u) \ne f(v)$

Ou seja, dois vértices adjacentes (ligados diretamente por uma aresta) **não podem** ter a mesma cor.

---

## Objetivo

Minimizar o número total de cores utilizadas. Esse valor mínimo é chamado de **número cromático** do grafo, denotado por $\chi(G)$.

---

## Número Cromático — Propriedades

* $\chi(G) = 1$ se $G$ não possui arestas (grafo nulo).
* $\chi(G) = 2$ se $G$ é bipartido e não trivial (ex: árvores).
* $\chi(G) \geq \Delta(G)$, onde $\Delta(G)$ é o grau máximo do grafo, **mas não necessariamente igual**.

**Teorema de Brooks**: Para um grafo conexo que não é um completo nem um ciclo ímpar, $\chi(G) \leq \Delta(G)$.

📚 **Fonte**: *West, D. B. (2001). Introduction to Graph Theory*. Prentice Hall.

---

## Problemas de Coloração

1. **Coloração de Vértices**: tradicional (como descrita acima).
2. **Coloração de Arestas**: cores em arestas, vizinhas não compartilham.
3. **Coloração de Faces**: usada em mapas (grafo planar).
4. **Coloração com Restrições**: listas de cores permitidas por vértice (List Coloring).
5. **Coloração de Caminho**: colorir caminhos ou ciclos específicos.

---

## Complexidade

A coloração de grafos é um problema **NP-difícil**. Determinar $\chi(G)$ é NP-completo para grafos arbitrários.

---

## Algoritmos Práticos

### Greedy (Guloso)

Implementação simples:

```python
for v in vértices:
    atribuir menor cor possível que não conflite com vizinhos
```

> Não garante o número cromático mínimo, mas é eficiente ($O(n^2)$ no pior caso).

### Estratégias no NetworkX (`greedy_color`)

* `'largest_first'`: vértices com maior grau primeiro.
* `'saturation_largest_first'`: também conhecido como **DSATUR**, prioriza vértices com maior "saturação" (número de cores diferentes nos vizinhos).
* `'random_sequential'`: ordem aleatória.
* `'smallest_last'`: remove o vértice com menor grau repetidamente, depois colore na ordem inversa.

---

## Aplicações Reais (Exemplos Detalhados)

### 1. **Horários em universidades**

Cada disciplina é um nó, e há uma aresta se duas disciplinas compartilham alunos → cores representam salas ou horários.

### 2. **Alocação de registradores**

No compilador, cada variável é um nó e há uma aresta se duas variáveis são vivas ao mesmo tempo. A cor representa um registrador físico.

### 3. **Pintura de Mapas**

Usado na formulação do famoso **Teorema das Quatro Cores** (todos mapas planos podem ser coloridos com no máximo 4 cores).


---

## Representação computacional

* **Grafo como dicionário ou matriz de adjacência**
* Algoritmos de coloração são implementados em bibliotecas como:

  * `networkx` (Python) (Que é a que estamos fazendo cobertura)
  * `igraph` (R, Python)
  * `Boost` (C++)

---

## Conclusão

A coloração de grafos é um problema essencial tanto em teoria quanto em aplicações práticas. Apesar da sua complexidade computacional, soluções heurísticas como o algoritmo guloso são amplamente utilizados com ótimos resultados em contextos reais.

---
