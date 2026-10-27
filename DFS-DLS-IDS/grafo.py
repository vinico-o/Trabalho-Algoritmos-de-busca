# No trabalho, cada vértice/estado representará uma estação
class Vertice:
    def __init__(self, nome, id_vertice, x, y, linha):
        self.nome = nome
        self.id = id_vertice

        # Coordenadas para o mapa
        self.x = float(x)
        self.y = float(y)

        self.linha = linha
        
        # Variáveis de controle das buscas
        self.cor = "branco" # Tag/Marcador
        self.pai = None     # Predecessor
        self.d = 0          # Tempo de descoberta
        self.f = 0          # Tempo de finalização
        self.adj = []       # Lista de vizinhos


class Grafo:
    def __init__(self):
        self.V = [] # Lista de vértices
        self.time = 0

    # Função para resetar o grafo entre buscas
    def resetar(self):
        for u in self.V:
            u.cor = "branco"
            u.pai = None
            u.d = 0
            u.f = 0
        self.time = 0