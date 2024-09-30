import json
import argparse
from bipartite import BipartiteGraph
from hopcroft import HopcroftKarp
def main():
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description='Processa um arquivo JSON para criar um grafo bipartido.')
    parser.add_argument('filename', type=str, help='O caminho do arquivo JSON contendo os dados do grafo')

    # Obtém os argumentos da linha de comando
    args = parser.parse_args()

    # Lê o arquivo JSON
    with open(args.filename, 'r') as file:
        data = json.load(file)
    
    # Converte listas de arestas em tuplas
    edges = set(tuple(edge) for edge in data['edges'])

    # Instancia o grafo bipartido
    graph = BipartiteGraph(data['U'], data['V'], edges)
    
    hopcroft = HopcroftKarp(graph)
    hopcroft.execute()
    # Imprime a representação do grafo
    print(graph)

if __name__ == "__main__":
    main()