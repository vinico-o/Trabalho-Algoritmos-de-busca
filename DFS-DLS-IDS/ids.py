# IDS (Iterative Deepening Search)
# Basicamente, executa o DLS várias vezes incrementando o limite a cada iteração

from dls import DLS

def IDS(G, origem, destino, limite_max=50):
    
    # Começamos com limite = 0
    limite = 0
    
    while limite <= limite_max:
        
        # Executa o DLS com o limite atual
        DLS(G, origem, limite)

        # Sabemos que encontramos a solução se a vértice destino foi descoberta (não é mais branco)
        if destino.cor != "branco":
            return limite
            
        # Se não encontrou, incremente o limite
        limite += 1
        
    # Se atingir o limite máximo e não achar, retorna falha
    return -1
