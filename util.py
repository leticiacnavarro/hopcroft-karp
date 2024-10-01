import networkx as nx
import matplotlib.pyplot as plt

def show_bipartite_graph(graph, marked_edges=None, layers=None, save=False, count=None):
    """
    Mostra o grafo bipartido usando NetworkX e Matplotlib, com vértices de U em azul e vértices de V em verde.
    Arestas marcadas são pintadas de vermelho. Se um vértice está no dicionário 'layers', exibe seu valor abaixo da bolinha do vértice.

    :param graph: Instância da classe BipartiteGraph.
    :param marked_edges: Conjunto de arestas que devem ser destacadas em vermelho.
    :param layers: Dicionário contendo valores dos vértices (nome do vértice como chave e valor como valor).
    """
    if marked_edges is None:
        marked_edges = set()

    if layers is None:
        layers = {}
    plt.figure(figsize=(5, 5))
    # Criar o grafo bipartido no NetworkX
    B = nx.Graph()

    # Adiciona os vértices de U (grupo 1) e de V (grupo 2)
    B.add_nodes_from(graph.U, bipartite=0)  # Conjunto U
    B.add_nodes_from(graph.V, bipartite=1)  # Conjunto V

    # Adiciona as arestas
    B.add_edges_from(graph.edges)

    # Gerar a posição bipartida dos vértices para o layout
    pos = nx.bipartite_layout(B, graph.U)


   # Colorir os vértices com base em 'marked_edges'
    marked_nodes = {u for u, v in marked_edges}.union({v for u, v in marked_edges})
    node_colors = ['#ff70a6' if node in marked_nodes else '#70d6ff' for node in B.nodes()]

    # Desenhar os vértices
    nx.draw(B, pos, 
            node_color=node_colors,
            node_size=2000)


    # Separar as arestas em normais e marcadas
    normal_edges = [edge for edge in B.edges() if edge not in marked_edges]
    red_edges = [edge for edge in B.edges() if edge in marked_edges]

    # Desenhar as arestas normais (cinza) e as marcadas (vermelho)
    nx.draw_networkx_edges(B, pos, edgelist=normal_edges, edge_color='#ffd670', width=3.3)
    nx.draw_networkx_edges(B, pos, edgelist=red_edges, edge_color='#ff9770', width=3.3)

    # Desenhar os rótulos dos vértices (nome dos vértices)
    nx.draw_networkx_labels(B, pos, font_size=18, font_color='black')

    # Desenhar os valores dos 'layers' abaixo dos vértices
    offset_pos = {node: (x, y - 0.10) for node, (x, y) in pos.items()}  # Desloca o rótulo para baixo
    layer_labels = {node: layers[node] for node in layers if node in B.nodes()}
    nx.draw_networkx_labels(B, offset_pos, labels=layer_labels, font_size=16, font_color='white')

    # Exibir o grafo
    if save:
        image_filename = f'image_{count}.png'
        plt.savefig(image_filename)
        plt.close()
        return image_filename
    else:
        plt.show()
        return None