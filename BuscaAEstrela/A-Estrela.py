class Estado:
    def __init__(self, valor, g, h, pai=None, acao= None):
        self.valor = valor # o estado representa o multiplicador acumulado
        self.g = g # custo real acumulado do caminho percorrido
        # na contextualizacao do problema, h é o número de operações realizadas,
        #por exemplo, se queremos ir de 1 até 1025, precisamos de 10 operacoes
        # de shift, ou seja 2^10 + 1 operacao de soma (logo: log2(x) + 1)
        self.h = h # custo estimado do restante do caminho
        self.f = g + h # f(n) = g(n) + h(n), custo estimado total do caminho
        self.pai = pai # estado pai (para reconstruir o caminho)
        self.acao = acao # ação que levou a este estado
    
    def __lt__(self, other) -> bool:
        return self.f < other.f

    #Começa no nó atual (destino) e sobe iterativamente pelos ponteiros self.pai até a raiz
    def reconstruir_caminho(self):
        pass

class Problema:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        #  na vida real o custo do shift é 1, assim como soma e subtracao
        self.operacoes = {
            "<< 1": (self.multiplicar_2, 2),
            ">> 1": (self.dividir_2, 2),
            "+ 1": (self.somar_1, 1),
            "- 1": (self.subtrair_1, 1)
        }
    
    def multiplicar_2(self, x):
        return x << 1

    def dividir_2(self, x):
        return x >> 1

    def somar_1(self, x):
        return x + 1

    def subtrair_1(self, x):
        return x - 1

class BuscaAEstrela:
    def __init__(self, problema, heuristica):
        pass
    
    def executar():
        pass
