from bipartite import BipartiteGraph
from util import show_bipartite_graph
import imageio
import os

class HopcroftKarp():
  def __init__(self, graph):
    """
    Implements Hopcroft-Karp Algoritm
    :param graph: Instância da classe BipartiteGraph.
    """
    self.graph = graph
    self.matching = set()
    self.layers = {}

    self.count = 0

  def execute(self):
    """
    Executa o algoritmo Hopcroft-Karp.
    :return: Conjunto de emparelhamentos.
    """
    
    while True:
      self.saving_image()

      self.find_graph_layers()      
      self.saving_image() 
      augmenting_paths = self.find_augmenting_path()

      if not augmenting_paths:
        break
      self.matching_union(augmenting_paths)

    print(f"Matching: {self.matching}")
    self.saving_gif()

  def find_graph_layers(self):
    unmatched_U = {u for u in self.graph.U if not any (u == match_u for match_u, match_v in self.matching)}
    self.layers = {}
    queue = sorted(list(unmatched_U))
    for u in unmatched_U:
      self.layers[u] = 0 # Definindo a camada inicial como 0.

    while queue:
      current = queue.pop(0)
      current_layer = self.layers[current]
      neighbors = sorted(self.graph.neighbors_U(current) | self.graph.neighbors_V(current))

      for neighbor in neighbors:
        if neighbor not in self.layers:
          self.layers[neighbor] = current_layer + 1
          queue.append(neighbor)
    self.layers = dict(sorted(self.layers.items()))
    return self.layers

  def is_in_matching(self, vertex):
      """
      Verifica se um vértice está no matching.

      :param vertex: O vértice a ser verificado.
      :return: True se o vértice estiver no matching, False caso contrário.
      """
      return any(vertex == match_u or vertex == match_v for match_u, match_v in self.matching)

  def find_augmenting_path(self):
      """
      Encontra caminhos aumentantes de V até U que não estão no matching e os armazena.

      :param layers: Dicionário de camadas gerado pela função find_graph_layers.
      """
      unmatched_V = sorted({v for v in self.graph.V if not any(v == match_v for match_u, match_v in self.matching)})

      augmenting_paths = []
      self.augmenting_paths = augmenting_paths

      for v in unmatched_V:
          # Inicia a busca a partir de v
          path = []
          if self.dfs(v, path):
              self.augmenting_paths.extend(path)  # Armazena o caminho encontrado
              self.layers.pop(v)
      return augmenting_paths

  def dfs(self, v, path):
      if v in self.graph.U and not self.is_in_matching(v):
        return True
      # if not self.is_in_matching(v):
      neighbors = sorted(self.graph.neighbors_U(v) | self.graph.neighbors_V(v))
      for u in neighbors:
          if u in self.layers:
            if self.layers[v] == self.layers[u] + 1:
              # Se o vértice u não estiver emparelhado ou se houver um caminho aumentante a partir de u
              if (not self.is_in_matching(u) or self.dfs(u, path)):
                  path.append([u,v])  # Adiciona u ao caminho
                  # path.append(v)  # Adiciona v ao caminho
                  self.layers.pop(u)

                  return True  # Caminho aumentante encontrado

      return False  # Nenhum caminho aumentante foi encontrado
      # return True
  def matching_union(self, augmenting_paths):
      """
      Atualiza o conjunto de emparelhamentos com base nos caminhos aumentantes.

      :param augmenting_paths: Lista de caminhos aumentantes.
      :return: O novo conjunto de emparelhamentos.
      """
      for path in augmenting_paths:
          self.saving_image()
          # Vamos iterar ao longo do caminho aumentante, alternando entre adicionar e remover arestas
          for i in range(len(path) - 1):
              u = path[i]
              v = path[i + 1]
              edge = (u, v) if u in self.graph.U else (v, u)

              if edge in self.matching:
                  # Se a aresta já está no matching, removemos ela
                  self.matching.remove(edge)
              else:
                  # Caso contrário, adicionamos ela ao matching
                  self.matching.add(edge)

      return self.matching

  def saving_image(self):
    if not self.count:
      self.count = 0
      self.image_files = []

    self.image_files.append(show_bipartite_graph(self.graph, marked_edges=self.matching, layers=self.layers, save=True, count=self.count))
    self.count = self.count + 1   

  def saving_gif(self):
    # Criar o GIF usando as imagens geradas
    gif_name = 'animation.gif'
    with imageio.get_writer(gif_name, mode='I', duration=1000, loop=0) as writer:
        for image_file in self.image_files:
            image = imageio.imread(image_file)
            writer.append_data(image)

    # Remover os arquivos de imagem temporários
    for image_file in self.image_files:
        os.remove(image_file)
