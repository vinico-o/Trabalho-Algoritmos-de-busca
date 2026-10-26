import numpy as np
from UCS import UCS


# bibliotecas para interface -> foi usado IA para gerar a Interface
import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
random.seed(42)
G = nx.Graph()

def main():
    inicial = 1
    final = 11

    grafo = {
        'MT': [('GO', np.random.randint(inicial, final)),
               ('MS', np.random.randint(inicial, final))],

        'GO': [('MG', np.random.randint(inicial, final)),
               ('MS', np.random.randint(inicial, final))],

        'MG': [('ES', np.random.randint(inicial, final)),
               ('RJ', np.random.randint(inicial, final)),
               ('SP', np.random.randint(inicial, final))],

        'ES': [('RJ', np.random.randint(inicial, final))],

        'MS': [('PR', np.random.randint(inicial, final)),
               ('SP', np.random.randint(inicial, final))],

        'PR': [('SC', np.random.randint(inicial, final))],

        'RJ': [('SP', np.random.randint(inicial, final))],

        'SC': [('RS', np.random.randint(inicial, final))],

        'SP': [('PR', np.random.randint(inicial, final))],

        'RS': []
    }


    
    """ interface gerada por IA """

    caminhos = []
    caminho_selecionado = None

    pos = {
        'MT': (0, 3),
        'GO': (1, 3),
        'MS': (1, 1.5),
        'MG': (2.5, 3),
        'ES': (4, 3.5),
        'RJ': (4, 2.5),
        'SP': (3.5, 1.5),
        'PR': (2.5, 0.5),
        'SC': (1.5, -0.5),
        'RS': (0.5, -1.5)
    }

    estados = list(grafo.keys())

    # função para aleatorizar os pesos pela interface 
    def aleatorizar_pesos():
        for estado in grafo:
            grafo[estado] = [
                (vizinho, np.random.randint(inicial, final))
                for vizinho, peso in grafo[estado]
            ]

        caminhos.clear()
        lista.delete(0, tk.END)
        caminho_selecionado = None
        desenhar_grafo()


    janela = tk.Tk()
    janela.title("Sistema de Busca de Rotas - UCS")
    janela.geometry("1200x750")

    texto_apresentacao = (
    "SISTEMA DE BUSCA DE ROTAS DE AJUDA (UCS)\n"
    "O estado do Rio Grande do Sul (RS) enfrenta enchentes\n"
    "que causam prejuízos à população e à infraestrutura.\n\n"
    "Mato Grosso (MT) busca uma rota para enviar ajuda ao RS.\n\n"
    "OBJETIVO:\n"
    "Encontrar caminhos entre os estados usando a UCS,\n"
    "priorizando os caminhos de menor custo acumulado."
    )

    ttk.Label(
        janela,
        text=texto_apresentacao,
        font=("Arial", 11),
        justify="center"
    ).pack(pady=10)

    estilo = ttk.Style()
    estilo.configure("TButton", padding=6)
    estilo.configure("TLabel", padding=4)

    painel = ttk.Frame(janela, padding=10)
    painel.pack(fill="x")

    ttk.Label(
        painel,
        text="SISTEMA DE BUSCA DE ROTAS DE AJUDA",
        font=("Arial", 16, "bold")
    ).grid(row=0, column=0, columnspan=5, pady=8)

    ttk.Label(painel, text="Estado de origem:").grid(row=1, column=0)

    origem_box = ttk.Combobox(
        painel, values='MT', state="readonly", width=8
    )
    origem_box.set("MT")
    origem_box.grid(row=1, column=1, padx=5)

    ttk.Label(painel, text="Estado de destino:").grid(row=1, column=2)

    destino_box = ttk.Combobox(
        painel, values='RS', state="readonly", width=8
    )
    destino_box.set("RS")
    destino_box.grid(row=1, column=3, padx=5)

    conteudo = ttk.Frame(janela, padding=10)
    conteudo.pack(fill="both", expand=True)

    painel_resultados = ttk.LabelFrame(
        conteudo, text="Caminhos encontrados", padding=8
    )
    painel_resultados.pack(side="left", fill="y", padx=(0, 10))

    lista = tk.Listbox(
        painel_resultados,
        width=48,
        height=25,
        font=("Consolas", 10),
        selectmode=tk.SINGLE
    )
    lista.pack(fill="y", expand=True)
    
    figura, ax = plt.subplots(figsize=(7, 6))
    canvas = FigureCanvasTkAgg(figura, master=conteudo)
    canvas.get_tk_widget().pack(side="right", fill="both", expand=True)

    def desenhar_grafo():
        ax.clear()

        for estado, ligacoes in grafo.items():
            for vizinho, peso in ligacoes:
                ax.annotate(
                    "",
                    xy=pos[vizinho],
                    xytext=pos[estado],
                    arrowprops=dict(
                        arrowstyle="->",
                        color="gray",
                        linewidth=1.3,
                        shrinkA=18,
                        shrinkB=18
                    )
                )

                meio_x = (pos[estado][0] + pos[vizinho][0]) / 2
                meio_y = (pos[estado][1] + pos[vizinho][1]) / 2
                ax.text(
                    meio_x, meio_y, str(peso),
                    fontsize=9,
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.8)
                )

        cores = []
        for estado in estados:
            if caminho_selecionado and estado in caminho_selecionado:
                cores.append("orange")
            else:
                cores.append("lightblue")

        xs = [pos[e][0] for e in estados]
        ys = [pos[e][1] for e in estados]

        ax.scatter(xs, ys, s=1100, c=cores, edgecolors="black", zorder=3)

        for estado in estados:
            ax.text(
                pos[estado][0], pos[estado][1], estado,
                ha="center", va="center",
                fontsize=10, fontweight="bold", zorder=4
            )

        if caminho_selecionado:
            for a, b in zip(caminho_selecionado, caminho_selecionado[1:]):
                ax.annotate(
                    "",
                    xy=pos[b],
                    xytext=pos[a],
                    arrowprops=dict(
                        arrowstyle="->",
                        color="red",
                        linewidth=3,
                        shrinkA=20,
                        shrinkB=20
                    ),
                    zorder=5
                )

        ax.set_title("Grafo de rotas de ajuda")
        ax.axis("off")
        figura.tight_layout()
        canvas.draw_idle()

    def selecionar_caminho(event=None):
        nonlocal_placeholder = None
        global caminho_selecionado

        selecao = lista.curselection()
        if not selecao or not caminhos:
            return

        indice = selecao[0]
        if indice >= len(caminhos):
            return

        caminho_selecionado = caminhos[indice][1].split("->")
        desenhar_grafo()

    def buscar_caminhos():
        nonlocal_placeholder = None
        global caminhos, caminho_selecionado

        origem = origem_box.get()
        destino = destino_box.get()

        caminhos = []
        caminho_selecionado = None
        lista.delete(0, tk.END)

        # aqui a interface usa o UCS
        resultados = UCS(grafo, origem, destino)

        for custo, caminho in resultados:
            lista.insert(tk.END, f"Custo {custo}: {caminho}")

        if not resultados:
            lista.insert(tk.END, "Nenhum caminho encontrado.")
            messagebox.showinfo(
                "Resultado", "Não foi encontrado um caminho."
            )
        else:
            lista.selection_set(0)
            selecionar_caminho()

        desenhar_grafo()

    lista.bind("<<ListboxSelect>>", selecionar_caminho)

    ttk.Button(
        painel,
        text="Buscar caminhos",
        command=buscar_caminhos
    ).grid(row=1, column=4, padx=10)

    ttk.Button(
        painel,
        text="Aleatorizar pesos",
        command=aleatorizar_pesos
    ).grid(row=1, column=5, padx=10)

    desenhar_grafo()
    janela.mainloop()

    

main()