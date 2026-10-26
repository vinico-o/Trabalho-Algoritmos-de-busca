class Heapq:
    def __init__(self):
        # A árvore binária representada como lista sequencial
        self.heap = []

    def esta_vazia(self):
        if len(self.heap) == 0:
            return True
        return False

    def inserir(self, estado):
        #insere o valor no final
        self.heap.append(estado)
        # coloca o elemento na posicao correta
        self.subir(len(self.heap) - 1)

    def extrair_minimo(self):
        if self.esta_vazia():
            return None

        # caso em que so existe 1 elemento, entao é so remover
        if len(self.heap) == 1:
            menor = self.heap.pop()
            return menor
        
        # removendo a raiz
        menor = self.heap[0]

        #move o último nó para a raiz e faz descer
        self.heap[0] = self.heap.pop()
        self.descer(0)

        return menor 
    
    def subir(self, i):
        pai = (i - 1) // 2
        
        # Enquanto não for a raiz e o f do nó for menor que o f do seu pai
        while i > 0 and self.heap[i].f < self.heap[pai].f:
            # Troca de posição
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            i = pai
            pai = (i - 1) // 2

    def descer(self, i):
        tamanho = len(self.heap)
        
        while True:
            esq = 2 * i + 1 
            dir = 2 * i + 2
            menor = i

            # Verifica se o filho da esquerda existe e tem f menor
            if esq < tamanho and self.heap[esq].f < self.heap[menor].f:
                menor = esq

            # Verifica se o filho da direita existe e tem f menor que o atual menor
            if dir < tamanho and self.heap[dir].f < self.heap[menor].f:
                menor = dir

            # Se o menor não for mais o próprio nó 'i', troca e continua descendo
            if menor != i:
                self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
                i = menor
            else:
                break
