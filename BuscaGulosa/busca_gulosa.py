from heap import MinHeap
# Grafo simplificado utilizado nos testes iniciais do algoritmo.
# A aplicação final utiliza o grafo carregado de mapa_lol.json.
coordenadas = {
    "Base": (0, 0),
    "Lobos": (2, 3),
    "Blue": (3, 1),
    "Rio": (6, 5),
    "Dragao": (9, 7)
}

grafo = {
    "Base": ["Lobos", "Blue"],
    "Lobos": ["Base", "Rio"],
    "Blue": ["Base", "Rio"],
    "Rio": ["Lobos", "Blue", "Dragao"],
    "Dragao": ["Rio"]
}

def heuristica(no_at,objetivo,coordenadas):
    x0,y0 = coordenadas[no_at]
    xn,yn = coordenadas[objetivo]
    deltax = x0-xn
    deltay = y0-yn
    deltax,deltay = deltax**2,deltay**2
    soma = deltax+deltay
    dist = soma ** (1/2)
    return dist

def busca_gulosa(grafo, ini,obj,coordenadas):
    fronteira = MinHeap()
    h_ini = heuristica(ini,obj,coordenadas)
    fronteira.inserir_min_heap((h_ini,ini))
    visitados = set()
    pai = {ini:None}
    expandidos = []
    
    while len(fronteira.heap)>0:
        front_heu,front_no = fronteira.extrair_min_heap()
        
        if front_no in visitados:
            continue
        visitados.add(front_no)
        
        if obj == front_no:
            resultado = reconstruir_caminho(pai,obj)
            return (resultado, expandidos)
        
        expandidos.append(front_no)
        lista_adj = grafo[front_no]
        for no in lista_adj:
            if no not in visitados and no not in pai:
                pai[no] = front_no
                heuri = heuristica(no,obj,coordenadas)
                fronteira.inserir_min_heap((heuri,no))
                
    return (None,expandidos)
       
def reconstruir_caminho(pais,objetivo):
    caminho = []
    no_at = objetivo
    while no_at != None:
        caminho.append(no_at)
        no_at = pais[no_at]
    caminho.reverse()
    return caminho


def rota_estrategica(grafo,objetivos,coordenadas):
    rota_completa = []
    estatisticas = []
    if not objetivos:
        return (rota_completa,estatisticas)
    if len(objetivos) == 1:
        return (objetivos,estatisticas)
    for i in range(len(objetivos)-1):
        caminho_trecho, expandidos_trecho = busca_gulosa(grafo,objetivos[i],objetivos[i+1],coordenadas)
        if caminho_trecho == None:
            return (None,estatisticas)
        dicio = {
            "origem":objetivos[i],
            "destino":objetivos[i+1],
            "caminho": caminho_trecho,
            "expandidos":expandidos_trecho,
            "qnt_expandidos": len(expandidos_trecho)
        }
        estatisticas.append(dicio)
        if not rota_completa:
            rota_completa.extend(caminho_trecho)
        else:
            rota_completa.extend(caminho_trecho[1:])
    return (rota_completa,estatisticas)
    
    
    
    
    
if __name__ == "__main__":
    print(heuristica("Lobos", "Dragao", coordenadas))
    print(heuristica("Rio", "Dragao", coordenadas))
    print(heuristica("Dragao", "Dragao", coordenadas))
    
    resultado = busca_gulosa(grafo, "Base", "Dragao", coordenadas)
    print("Caminho encontrado:", resultado)
    
    #Teste nele mesmo
    resultado = busca_gulosa(grafo, "Rio", "Rio", coordenadas)
    print("Teste 1:", resultado)

    #Teste caminho contrário
    resultado = busca_gulosa(grafo, "Dragao", "Base", coordenadas)
    print("Teste 2:", resultado)
    
    #Teste inacessível
    grafo_teste = grafo.copy()
    grafo_teste["Barao"] = []
    coordenadas_teste = coordenadas.copy()
    coordenadas_teste["Barao"] = (15, 15)
    resultado = busca_gulosa(
        grafo_teste,
        "Base",
        "Barao",
        coordenadas_teste
    )

    print("Teste 3:", resultado)
    
    #Teste com +de1 objetivo
    objetivos = ["Base", "Blue", "Rio", "Dragao"]

    resultado = rota_estrategica(grafo, objetivos, coordenadas)

    print("Rota estratégica:", resultado)
    print(rota_estrategica(grafo, [], coordenadas))
    print(rota_estrategica(grafo, ["Base"], coordenadas))
    print(rota_estrategica(grafo, ["Base", "Dragao"], coordenadas))
    
    #Teste das rotas com base nas estatisticas em cada nó explorado
    rota, estatisticas = rota_estrategica(
        grafo,
        ["Base", "Blue", "Rio", "Dragao"],
        coordenadas
    )
    print("Rota:", rota)

    for trecho in estatisticas:
        print(trecho["origem"], "->", trecho["destino"])
        print("Caminho:", trecho["caminho"])
        print("Expandidos:", trecho["expandidos"])
        print("Quantidade:", trecho["qnt_expandidos"])