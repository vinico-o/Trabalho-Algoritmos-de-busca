from asyncio import exceptions
from AEstrela import Problema, BuscaAEstrela
import networkx as nx
import matplotlib.pyplot as plt

def executar(inicio=None, destino=None, heuristica=True):

    print(f"Valor de Início: {inicio}")
    print(f"Valor de Destino: {destino}")
    problema = Problema(inicio, destino)
    
    if heuristica == True:
        busca_a_estrela = BuscaAEstrela(problema, usar_heuristica=True)
        solucao = busca_a_estrela.executar(problema, True)
    else:
        busca_a_estrela = BuscaAEstrela(problema, usar_heuristica=False)
        solucao = busca_a_estrela.executar(problema, False)

    if solucao:
        print(f"\nSolução encontrada em {len(solucao) - 1} passos:")
        print(f"Nós expandidos: {busca_a_estrela.nos_expandidos}")
        for no in solucao:
            print(f"Estado: {no.valor:>4} | Ação: {str(no.acao):>6} | g: {no.g:>2} | h: {no.h:>4.1f} | f: {no.f:>4.1f}")
    else:
        print("\nCaminho não encontrado!")

    limite = max(inicio, destino) * 2
    grafo = gerar_grafo(problema, limite)
    print(f"Número Total de Arestas geradas: {len(grafo)}")
    if heuristica == True:
        plotar_grafo(grafo, solucao)
    else:
        plotar_grafo(grafo, solucao, titulo="Grafo de Busca Dijkstra")


def gerar_grafo(problema, limite):
    arestas = []
    for x in range(1, limite + 1):
        for nome_acao, (funcao, _) in problema.operacoes.items():

            if nome_acao == ">> 1" and x % 2 != 0:
                            continue

            vizinho = funcao(x)
            # só aceita se estiver dentro do limite
            if 0 < vizinho <= limite and vizinho != x:
                arestas.append((x, vizinho, nome_acao))

    return arestas

def plotar_grafo(arestas, solucao=None, titulo="Grafo de Busca (A*)"):
    G = nx.DiGraph()

    #adiciona todas as arestas geradas no grafo
    for u, v, acao in arestas:
        G.add_edge(u, v, label=acao)

    #define o espacamento entre os nos
    pos = nx.spring_layout(G, seed=42, k=1.3)

    plt.figure(figsize=(11, 7))

    # destaca os elementos da solucao em outra cor
    nos_caminho = set()
    arestas_caminho = []
    if solucao:
        nos_caminho = {no.valor for no in solucao}
        for i in range(len(solucao) - 1):
            arestas_caminho.append((solucao[i].valor, solucao[i+1].valor))

    nos_normais = [n for n in G.nodes() if n not in nos_caminho]
    arestas_normais = [e for e in G.edges() if e not in arestas_caminho]

    #desenhar o grafo base
    nx.draw_networkx_nodes(G, pos, nodelist=nos_normais, node_color="#ecf0f1", node_size=400, edgecolors="#bdc3c7")
    nx.draw_networkx_edges(G, pos, edgelist=arestas_normais, edge_color="#bdc3c7", alpha=0.35, arrows=True, arrowsize=10)

    # desenhar a solucao em cor diferente
    if solucao:
        inicio_val = solucao[0].valor
        destino_val = solucao[-1].valor
        meio_vals = [no.valor for no in solucao[1:-1]]

        deslocamento = 0.04

        for i in range(len(solucao) - 1):
            atual = solucao[i]
            prox = solucao[i + 1]
            custo = prox.g - atual.g

            x1, y1 = pos[atual.valor]
            x2, y2 = pos[prox.valor]

            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2 + deslocamento

            plt.text(
                xm, ym, f"{prox.acao}, (c={custo})",
                color="#c0392b", fontsize=9, fontweight="bold",
                ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=0.5),
            )

        # Arestas da solução 
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, edge_color="#e74c3c", width=2.5, arrows=True, arrowsize=16)

        # Nós: Verde = Início, Vermelho = Destino, Laranja = Intermediários
        nx.draw_networkx_nodes(G, pos, nodelist=meio_vals, node_color="#f39c12", node_size=400, edgecolors="#d35400")
        nx.draw_networkx_nodes(G, pos, nodelist=[inicio_val], node_color="#2ecc71", node_size=400, edgecolors="#27ae60")
        nx.draw_networkx_nodes(G, pos, nodelist=[destino_val], node_color="#e74c3c", node_size=400, edgecolors="#c0392b")

    #define rótulo dos nós
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_color="#2c3e50")

    plt.title(titulo, fontsize=13, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
