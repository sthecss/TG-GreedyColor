## 🎨 Remember: Coloração de Grafos

A **coloração de vértices** em um grafo é o processo de atribuir uma "cor" (valor inteiro) a cada vértice de forma que **nenhum par de vértices adjacentes** (conectados por uma aresta) tenha a mesma cor.

---

## 🔢 Grau de um Vértice

* **Grau de um vértice**: número de arestas conectadas a ele.
* **Vértice de grau máximo**: o vértice com mais conexões.
* **Vértice de grau mínimo**: o vértice com menos conexões.

---

## 📊 Resumo do Grafo: *Les Misérables*

## **Vértices** (77):

Cada vértice representa um **personagem** da obra *Os Miseráveis*, de Victor Hugo. Os personagens incluem figuras centrais como **Jean Valjean, Javert, Cosette, Marius**, entre outros, bem como personagens secundários.

> ✔️ Total de vértices: **77 personagens**

---

## **Arestas** (254):

As arestas indicam **relações ou coocorrência** entre personagens — ou seja, dois personagens estão conectados se aparecem **juntos em alguma parte da história**. Quanto mais frequente a coocorrência, maior pode ser o peso da aresta (caso ponderado, embora aqui o grafo seja considerado não ponderado).

> ✔️ Total de arestas: **254 conexões**

> ✔️ O grafo é **conexo** — todos os personagens estão ligados direta ou indiretamente.

---

## 🎨 **Coloração**:

### 📈 **Vértice de grau máximo**

→ Personagem com **maior número de conexões** a outros personagens.
Ou seja:

> **É o personagem que aparece junto com mais outros personagens** — provavelmente **protagonista ou muito central na narrativa**.

📌 **Exemplo provável**: *Jean Valjean*.

---

### 📉 **Vértice de grau mínimo**

→ Personagem com **poucas ou até uma só conexão** com outros.
Ou seja:

> **É um personagem isolado ou periférico**, que aparece brevemente ou com poucos outros.

📌 **Exemplo provável**: personagens secundários que aparecem em só uma cena.

---

## 🎨 Na coloração, isso implica:

### ✅ Vértices de **grau máximo**:

* São mais difíceis de colorir (mais restrições).
* Tendem a receber cores **mais cedo** em estratégias como `largest_first` ou `saturation_largest_first`.

---

### ✅ Vértices de **grau mínimo**:

* São mais fáceis de colorir (menos restrições).
* Podem ser deixados para o final em estratégias como `smallest_last`.

---

## 🧠 Interpretação narrativa:

* O grau reflete o **nível de interação** do personagem no enredo.
* A coloração mostra **como separar** esses personagens em grupos que **não tem interação direta**.
* **Combinar os dois** (grau e cor) te ajuda a entender **quem é central e quem é periférico**, e como a história se organiza em **blocos de interação**.

---


## ⚙️ Estratégias de Coloração

### 1. `largest_first`

<img src="Imagens\largest_first.png" width="50%">


Ordena os vértices **do maior para o menor grau**. A ideia é colorir os vértices mais "difíceis" primeiro (os mais conectados), tentando minimizar conflitos mais cedo.

➡️ **Prioridade**: vértices de **grau máximo** primeiro.

---

### 2. `saturation_largest_first` (DSATUR)

<img src="Imagens\saturation_largest_first.png" width="50%">

Usa o algoritmo **DSATUR**: a cada passo, escolhe o vértice com o **maior número de cores diferentes** entre os seus vizinhos já coloridos (maior saturação). Em caso de empate, escolhe o de maior grau.

➡️ **Prioridade**: maior "pressão" para escolha de cor (maior saturação).

---

### 3. `smallest_last`

<img src="Imagens\smallest_last.png" width="50%">

Ordena os vértices para serem coloridos **do último ao primeiro**, onde a ordem é gerada removendo sucessivamente o vértice de **menor grau atual** do grafo.

➡️ **Prioridade**: o vértice colorido primeiro (por último na ordenação) tende a ser de **grau baixo**.

---

### 4. `random_sequential`

<img src="Imagens\random_sequential.png" width="50%">

Coloração em ordem aleatória. Pode dar resultados diferentes a cada execução, dependendo da semente aleatória.

➡️ **Prioridade**: nenhuma — ordem puramente aleatória.

---

### 5. `connected_sequential`

<img src="Imagens\connected_sequential.png" width="50%">

Começa de um vértice aleatório e percorre o grafo visitando vértices **adjacentes já visitados**, na ordem em que forem descobertos.

➡️ **Prioridade**: vértices próximos são coloridos sequencialmente.

---

### 6. `connected_sequential_bfs`

<img src="Imagens\connected_sequential_bfs.png" width="50%">

Parecido com o anterior, mas usa uma **busca em largura (BFS)**. Expande os vértices camada por camada.

➡️ **Prioridade**: vértices mais próximos da raiz, em largura.

---

### 7. `connected_sequential_dfs`

<img src="Imagens\connected_sequential_dfs.png" width="50%">

Similar ao anterior, mas usa **busca em profundidade (DFS)**. Vai fundo em um caminho antes de voltar.

➡️ **Prioridade**: vértices em caminhos profundos primeiro.

---

### 8. `independent_set`

<img src="Imagens\independent_set.png" width="50%">

Constrói conjuntos independentes (sem conexões entre si) e colore todos os vértices do mesmo conjunto com a mesma cor.

➡️ **Prioridade**: maximizar vértices que podem receber a mesma cor.

---

## 🧠 Comparação Estratégica

Cada estratégia tem desempenho diferente em diferentes tipos de grafos. Algumas tendem a usar menos cores em geral (como `dsatur`), enquanto outras são mais simples ou mais rápidas.

---
