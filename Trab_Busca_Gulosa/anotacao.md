# Busca Gulosa

- Escolhe o nó que parece estar mais perto do objetivo. f(n) = h(n)
    - Considera apenas o *futuro estimado*
    - Ignora o custo já gasto para chegar ao nó
    - Costuma encontrar soluções rapidamente
    - Não garante soluções ótimas
- Possui um estado inicuial e um objetivo, ai a heurística é a dist até objetivo. Lembrando que ela ignora o custo já percorrido.
- Não é completa, em geral. É completa em espaços finitos com controle de estados repetidos.
- Não é ótima, a heurística pode favorecer um caminho de custo total elevado.
- Tempo e espaço O(b^m) no pior caso.
- A heurística da busca gulosa aponta para o objetivo, mas ignora o custo já pago.
