# Busca Gulosa aplicada ao mapa de League of Legends

## Sobre o projeto

Este projeto apresenta uma implementação do algoritmo de Busca Gulosa (*Greedy Best-First Search*) em Python, aplicada a um grafo baseado no mapa de *League of Legends*.

O objetivo é encontrar um caminho entre dois pontos de interesse do mapa, como campos da selva, Dragão, Barão/Arauto e Aronguejos, utilizando a distância euclidiana como heurística para orientar a busca.

O algoritmo foi implementado separadamente da aplicação, permitindo utilizar diferentes grafos sem modificar sua lógica principal.

## Arquivos do projeto

```text
├── heap.py
├── busca_gulosa.py
├── mapa_lol.json
├── aplicacao_bgulosa_final.ipynb
└── README.md
```

- **heap.py:** implementação manual de uma min-heap, utilizada para manter os nós da fronteira ordenados pela prioridade.
- **busca_gulosa.py:** implementação da heurística euclidiana, da busca gulosa e da reconstrução do caminho encontrado.
- **mapa_lol.json:** contém os nós, as coordenadas e as conexões do mapa.
- **aplicacao_bgulosa_final.ipynb:** notebook responsável por carregar o mapa, permitir a escolha dos objetivos, executar a busca e visualizar os resultados.

## Representação do mapa

O mapa é representado por um grafo não direcionado, em que os nós cinzas indicam posições transitáveis e as arestas representam conexões possíveis entre essas posições.

O JSON utilizado contém 108 nós, dos quais 62 são considerados transitáveis, com 103 conexões entre eles.

Os monstros da selva e os objetivos do rio são representados separadamente dos pontos de passagem. Para permitir sua seleção como origem ou destino, cada objetivo é associado automaticamente ao nó transitável geometricamente mais próximo.

Essa associação é uma aproximação baseada nas coordenadas do mapa e não necessariamente representa a entrada real do objetivo dentro do jogo.

## Funcionamento da busca gulosa

A Busca Gulosa utiliza uma função heurística para escolher qual nó da fronteira será explorado primeiro.

Neste projeto, a heurística utilizada é a distância euclidiana:

\[
h(n) = \sqrt{(x_n-x_d)^2+(y_n-y_d)^2}
\]

Em que \(n\) é o nó analisado e \(d\) é o nó de destino.

Os nós da fronteira são armazenados em uma min-heap implementada manualmente. A cada iteração, o algoritmo seleciona o nó com o menor valor heurístico, verifica se ele é o objetivo e, caso contrário, examina seus vizinhos.

Quando o destino é encontrado, o caminho é reconstruído a partir dos predecessores registrados durante a busca.

A Busca Gulosa utiliza somente a estimativa heurística para orientar a exploração e, portanto, não garante encontrar o caminho de menor custo.

## Como executar

### Requisitos

- Python 3
- Jupyter Notebook ou VS Code com as extensões Python e Jupyter
- Bibliotecas `matplotlib` e `ipywidgets`

Para instalar as dependências, execute no terminal:

```bash
python -m pip install matplotlib ipywidgets ipykernel
```

### Execução

1. Mantenha os arquivos do projeto na mesma pasta.
2. Abra `aplicacao_bgulosa_final.ipynb` no VS Code ou Jupyter.
3. Selecione o ambiente Python correspondente.
4. Execute as células em ordem, utilizando **Run All**.
5. Na seção de execução da busca, escolha a origem e o destino nos menus suspensos.
6. Execute novamente as células de busca, visualização e resultados quando alterar os objetivos.

O notebook exibirá o caminho encontrado sobre o grafo e um resumo contendo a origem, o destino, a sequência de nós percorridos e a quantidade de nós expandidos.

## Visualização e validação

Na visualização, as conexões transitáveis aparecem em cinza, o caminho encontrado em verde, a origem em azul e o destino em vermelho.

O programa também verifica se cada par de nós consecutivos do caminho possui uma conexão no grafo, permitindo confirmar se o percurso encontrado é válido.

A validação considera a conectividade do grafo utilizado e não simula todas as regras de movimentação presentes no jogo.

## Considerações finais

A aplicação demonstra o funcionamento da Busca Gulosa em um cenário de navegação baseado no mapa de *League of Legends*.

A utilização do grafo permite representar os caminhos disponíveis, enquanto a heurística euclidiana orienta a exploração em direção ao objetivo selecionado.

O projeto não considera condições dinâmicas de uma partida, como visão inimiga, movimentação de campeões ou alterações no estado das estruturas. Seu foco é a aplicação do algoritmo de busca sobre um grafo estático.

---

*Este README foi elaborado com auxílio de inteligência artificial, com o objetivo de organizar e facilitar a compreensão da implementação e do funcionamento do projeto.*