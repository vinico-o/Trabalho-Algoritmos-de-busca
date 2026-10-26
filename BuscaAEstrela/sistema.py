from asyncio import exceptions
from AEstrela import Problema, BuscaAEstrela
import networkx as nx
import matplotlib.pyplot as plt

def apresentacao():
    print("APLICAÇÃO DO ALGORITMO DE BUSCA A*\n")
    print("Em processadores embarcados, a multiplicação e divisão de numeros e uma operação muito custosa")
    print("em termos de ciclos de clock.")
    print("")
    print("Por esta razão, compiladores utilizam otimizações para reduzir")
    print("o custo de operações matematicas. No entanto, esta é uma tarefa complexa,")
    print("pois pode envolver a criação de muitas operações, o que aumentaria o")
    print("tamanho do código e o tempo de execução.")
    print("")
    print("O objetivo deste trabalho é implementar o algoritmo de Busca A* para ")
    print("encontrar a sequência de operações mais curta para multiplicar ou dividir um número ")
    print("por uma constante, utilizando operações de soma, subtração e shift de bits.")


def main():
    apresentacao()

    inicio = int(input("Digite o número inicial: "))
    destino = int(input("Digite o número final: "))
    problema = Problema(inicio, destino)
    
    busca_a_estrela = BuscaAEstrela(problema, usar_heuristica=True)
    solucao = busca_a_estrela.executar(problema, True)

    if solucao:
        print(f"\nSolução encontrada em {len(solucao) - 1} passos:")
        print(f"Nós expandidos: {busca_a_estrela.nos_expandidos}")
        for no in solucao:
            print(f"Estado: {no.valor:>4} | Ação: {str(no.acao):>6} | g: {no.g:>2} | h: {no.h:>4.1f} | f: {no.f:>4.1f}")
    else:
        print("\nCaminho não encontrado!")

    limite = max(inicio, destino) * 2
    grafo = gerar_grafo(problema, limite)
    print(len(grafo))
    plotar_grafo(grafo, solucao)


def gerar_grafo(problema, limite):
    arestas = []
    for x in range(1, limite + 1):
        for nome_acao, (funcao, _) in problema.operacoes.items():

            if nome_acao == ">> 1" and x % 2 != 0:
                            continue

            vizinho = funcao(x)
            # Só aceita se estiver dentro do tabuleiro delimitado
            if 0 < vizinho <= limite and vizinho != x:
                arestas.append((x, vizinho, nome_acao))

    return arestas

def plotar_grafo(arestas, solucao=None):
    G = nx.DiGraph()

    #adiciona todas as arestas geradas no grafo
    for u, v, acao in arestas:
        G.add_edge(u, v, label=acao)

    #define o espacamento entre os nos
    pos = nx.spring_layout(G, seed=42, k=1.3)

    plt.figure(figsize=(11, 7))

    # 3. Separar elementos da solução para destacar
    nos_caminho = set()
    arestas_caminho = []
    if solucao:
        nos_caminho = {no.valor for no in solucao}
        for i in range(len(solucao) - 1):
            arestas_caminho.append((solucao[i].valor, solucao[i+1].valor))

    nos_normais = [n for n in G.nodes() if n not in nos_caminho]
    arestas_normais = [e for e in G.edges() if e not in arestas_caminho]

    # 4. Desenhar o grafo base (fundo suave)
    nx.draw_networkx_nodes(G, pos, nodelist=nos_normais, node_color="#ecf0f1", node_size=600, edgecolors="#bdc3c7")
    nx.draw_networkx_edges(G, pos, edgelist=arestas_normais, edge_color="#bdc3c7", alpha=0.35, arrows=True, arrowsize=10)

    # 5. Desenhar o caminho da solução em destaque
    if solucao:
        inicio_val = solucao[0].valor
        destino_val = solucao[-1].valor
        meio_vals = [no.valor for no in solucao[1:-1]]

        # Arestas da solução (vermelho escuro e grossas)
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, edge_color="#e74c3c", width=2.5, arrows=True, arrowsize=16)

        # Nós: Verde = Início, Vermelho = Destino, Laranja = Intermediários
        nx.draw_networkx_nodes(G, pos, nodelist=meio_vals, node_color="#f39c12", node_size=750, edgecolors="#d35400")
        nx.draw_networkx_nodes(G, pos, nodelist=[inicio_val], node_color="#2ecc71", node_size=850, edgecolors="#27ae60")
        nx.draw_networkx_nodes(G, pos, nodelist=[destino_val], node_color="#e74c3c", node_size=850, edgecolors="#c0392b")

    # 6. Rótulos dos nós (números)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_color="#2c3e50")

    plt.title("Grafo de Busca com Solução Ótima Destacada (A*)", fontsize=13, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()