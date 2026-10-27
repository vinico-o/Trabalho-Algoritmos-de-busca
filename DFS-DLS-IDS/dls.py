# DLS (Depth-Limited Search / Busca em Profundidade Limitada)
# Basicamente, um DFS com limite de profundidade

def DLS(G, raiz, limite):
    
    # Inicialização dos vértices (apenas se executar mais de uma vez)
    G.resetar()
    
    # Começa a busca a partir de um estado inicial (raiz)
    dls_visit(G, raiz, limite, 0)


                          # profundidade atual
def dls_visit(G, u, limite, prof_atual):

    # Vértice 'u' acaba de ser descoberta
    G.time += 1
    u.d = G.time
    u.cor = "cinza"
    
    # Só exploramos as arestas se a profundidade atual for MENOR que o limite
    # Ao chegar na profundidade do limite (l), o algoritmo não gera/descobre os filhos daquele vértice/nó
    if prof_atual < limite:
        for v in u.adj:
            if v.cor == "branco":
                v.pai = u
                
                # Desce um nível incrementando a profundidade
                dls_visit(G, v, limite, prof_atual + 1)
            
    # Vértice 'u' foi finalizada (preto)
    u.cor = "preto"
    G.time += 1
    u.f = G.time
