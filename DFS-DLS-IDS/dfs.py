# DFS

def DFS(G, raiz):

    # Inicialização das vértices
    G.resetar()

    # Iniciamos a busca por DFS
    dfs_visit(G, raiz)

    # Visita todos os componentes do grafo (até se forem isolados)
    #for u in G.V:
#
#        # Se o vértice atual ainda não foi explorado, exploramos ele
#        if u.cor == "branco":
#            dfs_visit(G, u)


# Função para exploração
def dfs_visit(G, u):

    # Vértice branca 'u' acaba de ser descoberta (cinza)
    G.time += 1
    u.d = G.time
    u.cor = "cinza"
    
    # Explora a aresta (u, v) (vizinhos)
    for v in u.adj:
        if v.cor == "branco":
            v.pai = u
            dfs_visit(G, v)
            
    # Vértice 'u' foi finalizada (preto)
    u.cor = "preto"
    G.time += 1
    u.f = G.time
