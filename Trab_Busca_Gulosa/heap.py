class MinHeap:
    def __init__(self):
        self.heap = [] #lista que armaz os elementos
        
    def inserir_min_heap(self,elemento):
        #Sabemos que o elemento é composto pela tupla entre o valor da heurística e o nome do nó
        #O elemento seria algo como: (valor_heurística, nome_no)
        self.heap.append(elemento)
        self.subir_heap()
        
    def subir_heap(self):
        ind_inserido = len(self.heap) -1
        pai_do_inserido = (ind_inserido-1)//2
        fez_troca = True
        while  fez_troca and ind_inserido>0:
                if self.heap[ind_inserido][0]<self.heap[pai_do_inserido][0]:
                    self.heap[ind_inserido],self.heap[pai_do_inserido] = self.heap[pai_do_inserido], self.heap[ind_inserido]
                    ind_inserido = pai_do_inserido
                    pai_do_inserido = (ind_inserido-1)//2
                else:
                    fez_troca = False
                    
    def extrair_min_heap(self):
        if  not self.heap:
            return None
        
        min_do_heap = self.heap[0]
        if len(self.heap)>1:
            self.heap[0] = self.heap.pop(-1)
            self.descer_heap()
        elif len(self.heap) == 1:
            self.heap.pop(0)
        return min_do_heap            
                
    def descer_heap(self):
        ind_atual = 0
        fez_troca = True
        while fez_troca:
            ind_menor = ind_atual
            fi_esq = 2*ind_atual +1
            fi_dir = 2*ind_atual +2
            if fi_esq < len(self.heap) and self.heap[fi_esq][0] < self.heap[ind_menor][0]:
                ind_menor = fi_esq
            if fi_dir < len(self.heap) and self.heap[fi_dir][0] < self.heap[ind_menor][0]:
                ind_menor = fi_dir
            
            if ind_menor != ind_atual:
                self.heap[ind_menor],self.heap[ind_atual] = self.heap[ind_atual],self.heap[ind_menor]
                ind_atual = ind_menor

            else:
                fez_troca = False
        
                     
if __name__ == "__main__":
    fila = MinHeap()
    
    fila.inserir_min_heap((8 ,"Lobos"))
    print(fila.heap)
    fila.inserir_min_heap((5, "Rio"))
    print(fila.heap)
    fila.inserir_min_heap((12, "Blue"))
    print(fila.heap)
    fila.inserir_min_heap((3, "Dragao"))
    print(fila.heap)
    fila.inserir_min_heap((1, "Barao"))
    print(fila.heap)    
    
    print("\nTestando extrações:")

    while fila.heap:
        minimo = fila.extrair_min_heap()
        print("Removido:", minimo)
        print("Heap restante:", fila.heap)
    
    fila_vazia = MinHeap()
    print(fila_vazia.extrair_min_heap())
    
    fila_unica = MinHeap()
    fila_unica.inserir_min_heap((7, "Red"))

    print(fila_unica.extrair_min_heap())
    print(fila_unica.heap)