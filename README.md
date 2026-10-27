# Algoritmos de Busca

Este repositório reúne implementações de diferentes algoritmos de busca e exemplos de execução. Em cada projeto, os arquivos do **núcleo** implementam a busca (e suas estruturas auxiliares); os arquivos de **execução e visualização** montam o cenário, acionam os algoritmos e apresentam os resultados.

## Visão geral dos arquivos

| Projeto | Núcleo da busca | Execução e visualização |
| --- | --- | --- |
| **Busca em Largura (BFS)** | `BFS/lol_gank_bfs.py` — contém a função `bfs` e também a lógica do cenário. | `BFS/lol_gank_bfs.py` — a função `executar` configura e executa a simulação e apresenta o passo a passo e o resultado. O notebook `BFS/LOL_Gank_BFS.ipynb` contém a versão em notebook da demonstração. |
| **Busca A\*** | `BuscaAEstrela/AEstrela.py` — estados, problema e algoritmo A\*. `BuscaAEstrela/Heapq.py` — fila de prioridade (min-heap) usada pela busca. | `BuscaAEstrela/sistema.py` — coordena a execução, imprime os dados da solução e desenha o grafo. `BuscaAEstrela/execucao.ipynb` — exemplo de uso e comparação com a busca sem heurística. |
| **Busca Gulosa** | `BuscaGulosa/busca_gulosa.py` — heurística, busca gulosa, reconstrução do caminho e montagem de rotas por objetivos. `BuscaGulosa/heap.py` — min-heap auxiliar. | `BuscaGulosa/aplicacao_bgulosa_final.ipynb` — carrega o mapa, permite selecionar pontos, executa a busca e visualiza a rota. |
| **Busca de Custo Uniforme (UCS)** | `BuscaUCS/UCS.py` — implementação da UCS e min-heap utilizada por ela. | `BuscaUCS/interface.py` — cria a interface gráfica, prepara o grafo com pesos, aciona a UCS e mostra os caminhos encontrados. |
| **DFS, DLS e IDS** | `DFS-DLS-IDS/dfs.py` — busca em profundidade; `DFS-DLS-IDS/dls.py` — busca em profundidade limitada; `DFS-DLS-IDS/ids.py` — aprofundamento iterativo, que reutiliza DLS. `DFS-DLS-IDS/grafo.py` fornece as estruturas `Grafo` e `Vertice` compartilhadas pelas buscas. | `DFS-DLS-IDS/simulacao.ipynb` — carrega a rede, executa os algoritmos e apresenta a visualização das estações e da rota. |

## Arquivos de dados e documentação

- `BuscaGulosa/mapa_lol.json`: nós, coordenadas e conexões usados pela aplicação de Busca Gulosa.
- `DFS-DLS-IDS/estacoes.csv` e `DFS-DLS-IDS/conexoes.csv`: dados da rede carregados pela simulação de DFS/DLS/IDS.
- `BFS/feita no graphlab matrix (1).csv` e `BFS/feito no graphlab (1).png`: arquivos de apoio do mapa do projeto de BFS.
- `BuscaGulosa/README.md`: documentação específica da Busca Gulosa, incluindo requisitos e instruções de execução.
- `DFS-DLS-IDS/relatorio.md` e `BuscaUCS/Uso de IA.md`: documentação complementar dos respectivos projetos.

## Como começar

Para executar um exemplo, abra o notebook indicado na tabela em Jupyter ou no VS Code com suporte a Python/Jupyter e execute as células em ordem. A interface da UCS é um script Python separado; seus requisitos de interface gráfica e bibliotecas precisam estar instalados no ambiente Python.