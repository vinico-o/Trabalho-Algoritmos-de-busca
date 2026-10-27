# Relatório

## 1. Cenário

O trabalho simula o trajeto em uma rede de estações de metrô. Cada estação é um vértice e cada conexão entre duas estações é uma aresta. Os dados da rede são carregados pelos arquivos `estacoes.csv` e `conexoes.csv`.

O notebook `simulacao.ipynb` executa algoritmos de busca sobre esse grafo e apresenta a rota encontrada em um mapa.

## 2. Como utilizar a simulação

Para executar a simulação:

1. Abra `simulacao.ipynb` no Jupyter ou no VS Code.
2. Execute as células na ordem.
3. Verifique se os arquivos `estacoes.csv` e `conexoes.csv` estão na mesma pasta do notebook.
4. Execute a célula de execução e, depois, a célula **Plotar Mapa**.

A célula de carregamento lê os CSVs, cria os objetos `Vertice`, adiciona-os ao objeto `Grafo` e preenche as listas de adjacência. A célula de execução realiza as buscas e a célula do mapa destaca a rota encontrada pelo IDS.

## 3. Como alterar o trajeto

O trajeto é definido na célula de execução do notebook, na terceira célula de código. Altere estas linhas:

```python
origem = "23"   # <----- altere para qualquer ID de outra estação
destino = "27"  # <----- basta ver em estacoes.csv

origem_vertice = vertices[origem]
destino_vertice = vertices[destino]

limite_dls = 14 # <----- limite dls (não deixe menor que o necessário)
```

## 4. Uso de IA

Todos algoritmos foram implementados manualmente, utilizando como base o livro _Introduction to Algorithms_, de Thomas H. Cormen.

O uso de IA foi somente para gerar o gráfico/mapa de visualização das estações e da rota encontrada.