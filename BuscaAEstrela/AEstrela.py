import numpy as np
from Heapq import Heapq

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

    #Começa no nó atual (destino) e sobe iterativamente pelos ponteiros self.pai até a raiz
    def reconstruir_caminho(self):
        caminho = []
        atual = self
        while atual is not None:
            caminho.append(atual)
            atual = atual.pai
        return caminho[::-1] # retorna o caminho na ordem contraria

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

    def calcular_heuristica(self, valor):
        # se eu ja cheguei no destino, minha heurística é zero
        if valor == self.destino:
            return 0.0
        # se meu valor é maior que o destino, 
        # eu devo retornar por meio de subtracoes
        elif valor > self.destino:
            return valor - self.destino
        # se meu valor é menor que o destino,
        # eu ando por meio de multiplicaçoes por 2
        # por exemplo de 256 -> 1024. o número de operaçoes é
        # 256 x 2^k = 1024 => k = log2(1024/256) = 2
        elif valor < self.destino:
            return float(np.floor(np.log2(self.destino / valor)))
    
    def multiplicar_2(self, x):
        return x << 1

    def dividir_2(self, x):
        return x >> 1

    def somar_1(self, x):
        return x + 1

    def subtrair_1(self, x):
        return x - 1

class BuscaAEstrela:
    def __init__(self, problema, usar_heuristica=True, grafo=None):
        self.problema = problema
        self.usar_heuristica = usar_heuristica

        self.nos_expandidos = 0
        self.caminho_solucao = 0
    
    def executar(self, problema, heuristica):
        #Criacao do Nó raiz
        #Caso heuristica seja true, calcula o A*
        #se nao, realiza praticamente um Djikstra
        if heuristica == True:
            raiz = Estado(problema.inicio, 0, problema.calcular_heuristica(problema.inicio))
        else:
            raiz = Estado(problema.inicio, 0, 0)
        
        # inserir a raiz na fila do heap
        fronteira = Heapq()
        fronteira.inserir(raiz)

        # chave é o valor numerico do estado
        # o valor é o menor custo para chegar naquele estado
        melhores_g = {raiz.valor: 0}

        while  not fronteira.esta_vazia():
            #encontro o menor f(n) entre os estados e extraio ele
            atual = fronteira.extrair_minimo()

            # verifica se o custo g atual é maior que o melhor,
            #pois dessa forma nao é necessário explorar
            # caso o estado ainda nao tenha outro g registrado, devolve inf
            if atual.g > melhores_g.get(atual.valor, float('inf')):
                continue

            # verifica se chegamos no final (encontramos a solucao)
            if problema.destino == atual.valor:
                solucao = atual.reconstruir_caminho()
                self.caminho_solucao += 1
                return solucao

            else: 
                # Expansao para os nos vizinhos
                for acao, (funcao, custo) in problema.operacoes.items():
                    #realiza o calculo respectivo para o vizinho
                    novo_valor = funcao(atual.valor)

                    #evita numeros menores iguais a zero
                    if novo_valor <= 0:
                        continue

                    #calcula o novo custo acumulado do caminho ja percorrido
                    novo_g = atual.g + custo

                    #avaliacao se o caminho atual é mais vantajoso
                    if novo_g < melhores_g.get(novo_valor, float('inf')):

                        #atualiza o menor custo registrador
                        melhores_g[novo_valor] = novo_g

                        #calcula a heuristica
                        if heuristica == True:
                            novo_h = problema.calcular_heuristica(novo_valor)
                        else:
                            #caso do djikstra comum, sem heuristica
                            novo_h = 0

                        #cria o novo no e insere na fila
                        sucessor = Estado(novo_valor, novo_g, novo_h, atual, acao)
                        fronteira.inserir(sucessor)
                        self.nos_expandidos += 1

        print("Caminho nao Encontrado!")
        return []
            
            



