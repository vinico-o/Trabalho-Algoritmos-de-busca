# heap baseado no trabalho de redes (Dijkstra) 
class MinHeap:

    def __init__(self):
        self.heap = []

    # colocar item no heap
    def push(self, item):
        self.heap.append(item)

        # ajusta a posicao do item inserido (q esta no final)
        self._subir(len(self.heap) - 1)

    # retira o item com o menor valor
    def pop(self):
        
        # troca o 1 com o ultimo
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]

        item = self.heap.pop()
    
        self._descer(0)
        return item

    # sobe o item no heap e ordena
    def _subir(self, i):

        # pega o valor do pai
        pai = (i - 1) // 2

        # enquanto o filho (i) for menor que o pai (pai), vai realizar trocas (subir)
        if i > 0 and self.heap[i][0] < self.heap[pai][0]:
            
            self.heap[pai], self.heap[i] = self.heap[i], self.heap[pai]
            
            self._subir(pai)

    # desce o item e ordena
    def _descer(self, i):
        
        # pega os filhos da raiz (i)
        menor = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        # se o filho esq existe e é menor q o atual (i) -> atualiza o menor
        if esq < len(self.heap) and self.heap[esq][0] < self.heap[menor][0]:
            menor = esq
        
        # o contrário do if de cima
        if dir < len(self.heap) and self.heap[dir][0] < self.heap[menor][0]:
            menor = dir
        
        # se o menor nn for o atual -> (ou seja, entrou em algum if de cima) -> troca
        if menor != i:

            self.heap[menor], self.heap[i] = self.heap[i], self.heap[menor]
            
            # chama dnv para garantir que o menor esteja no topo
            self._descer(menor)

    # da o tamanho do heap
    def __len__(self):
        return len(self.heap)


def UCS(grafo, raiz, destino): 

    hp = MinHeap()

    if raiz == destino:
        return

    hp.push((0, raiz))

    encontrado = False

    resultados = []

    while hp:

        custo_acumulado, tmp = hp.pop()

        # se a última letra do caminho (nó atual) for o destino - encontramos um caminho
        if tmp[-2:] == destino:

            resultados.append((custo_acumulado, tmp))
            encontrado = True

        # buscamos as ligações do nó atual
        ligacoes = grafo[tmp[-2:]]

        # joga no heap as ligações do nó atual com os caminhos + custo
        for i in range (len(ligacoes)):
            hp.push((custo_acumulado + ligacoes[i][1], f'{tmp}->{ligacoes[i][0]}'))

    if encontrado == False:
        return []

    resultados.sort()
    return resultados

