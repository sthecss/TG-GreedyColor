import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Caso queira menos grafos, torne linhas do (i) em comentários
# Caso queira testar menos estratégias, torne linhass do (ii) em comentários

# Passo (i) Dicionário de grafos
grafos = {
    #"Petersen": nx.petersen_graph(),
    #"Mycielski (4)": nx.mycielski_graph(4),
    #"Desargues": nx.desargues_graph(),
    #"K_{3,3,3}": nx.complete_multipartite_graph(3, 3, 3),
    #"Aleatório Denso": nx.gnp_random_graph(20, 0.4, seed=42),
    "Os miseraveis": nx.les_miserables_graph()
}

# Passo (ii) Estratégias de coloração
estrategias = [
    "largest_first",
    "saturation_largest_first",
    "smallest_last",
    "random_sequential",
    "connected_sequential",
    "connected_sequential_bfs",
    "connected_sequential_dfs",
    "independent_set"
]

# ==================================================================
#                       PLOTAGEM DO GRAFO:
# ==================================================================

def visualizar_grafo(grafo, nome_grafo, estrategia, coloracao):
    # 1. Cria uma figura com tamanho definido (largura=20, altura=15)
    plt.figure(figsize=(20, 15))

    # 2. Calcula a posição dos nós no gráfico usando o layout de força (spring_layout)
    #    - 'seed=42' garante que o layout seja reproduzível!
    #    - 'k' e 'iterations' ajustam a distância entre os nós e a estabilidade
    pos = nx.spring_layout(grafo, seed=42, k=3.5, iterations=600)

    # 3. Cria a barra de cores (colorbar) para mostrar o mapeamento das cores usadas na coloração
    cbar = plt.colorbar(
        plt.cm.ScalarMappable(
            cmap=plt.cm.tab20,  # Mapa de cores com até 20 cores distintas
            norm=plt.Normalize(vmin=0, vmax=max(coloracao.values()))
        ),
        ax=plt.gca()
    )
    cbar.set_ticks(range(len(set(coloracao.values()))))  # Define onde os valores aparecem na barra

    # 4. Desenha os nós do grafo
    nx.draw_networkx_nodes(
        grafo, pos,
        node_color=[coloracao[n] for n in grafo.nodes()],  # Cor de cada nó, baseada na coloração
        cmap=plt.cm.tab20,  # Mesmo mapa de cores da colorbar
        node_size=600,      # Tamanho dos nós
        edgecolors='black'  # Contorno preto nos nós
    )

    # 5. Desenha as arestas (ligações entre os nós)
    nx.draw_networkx_edges(
        grafo, pos,
        width=1.0,          # Espessura da linha
        alpha=0.4,          # Transparência
        edge_color='gray'   # Cor das arestas
    )

    # 6. Adiciona os rótulos dos nós (nome dos personagens ou identificadores)
    labels = {n: str(n) for n in grafo.nodes()}
    nx.draw_networkx_labels(
        grafo, pos,
        labels=labels,
        font_size=6,
    )

    # 7. Título informativo do grafo, com nome, estratégia usada, número de cores, nós e arestas
    plt.title(
        f"Grafo: {nome_grafo}\n"
        f"Estratégia: {estrategia.upper()} | "
        f"Cores usadas: {max(coloracao.values()) + 1}\n"
        f"Nós: {grafo.number_of_nodes()} | Arestas: {grafo.number_of_edges()}"
    )

    # 8. Remove os eixos e ajusta o layout final para melhor apresentação
    plt.axis('off')
    plt.tight_layout()
    plt.show()


# ==================================================================
#                  ANALISE E COLORACAO DO GRAFO:
# ==================================================================

print("=" * 50)
print("ANÁLISE DE COLORAÇÃO DE GRAFOS")
print("=" * 50 + "\n")

for nome_grafo, G in grafos.items():
    print(f"\n🔷 GRAFO: {nome_grafo.upper()}")
    print(f"• Nós: {G.number_of_nodes()}")
    print(f"• Arestas: {G.number_of_edges()}")
    print(f"• Conexo: {'Sim' if nx.is_connected(G) else 'Não'}")

    resultados = []
    for estrategia in estrategias:
        try:
            coloracao = nx.coloring.greedy_color(G, strategy=estrategia) # COLORACAO OCORRE AQUI HEIN
            num_cores = len(set(coloracao.values()))
            resultados.append((estrategia, num_cores))

            print(f"\n  ⚙️ {estrategia.upper()}: {num_cores} cores")

            visualizar_grafo(G, nome_grafo, estrategia, coloracao)

        except Exception as e:
            print(f"  ❌ Erro em {estrategia}: {str(e)}")
            continue

    print("\n  📋 MELHORES ESTRATÉGIAS:")
    for estrategia, cores in sorted(resultados, key=lambda x: x[1])[:3]:
        print(f"  {estrategia.ljust(25)} → {cores} cores")
    print("=" * 50)
