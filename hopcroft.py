from bipartite import BipartiteGraph
from util import show_bipartite_graph
class HopcroftKarp():
  def __init__(self, graph):
    """
    Implements Hopcroft-Karp Algoritm
    :param graph: Instância da classe BipartiteGraph.
    """
    self.graph = graph
    self.matching = set()
    self.layers = {}

  def execute(self):
    """
    Executa o algoritmo Hopcroft-Karp.
    :return: Conjunto de emparelhamentos.
    """

    while True:
      self.find_graph_layers()
      print(self.layers)
      show_bipartite_graph(self.graph, marked_edges=self.matching, layers=self.layers)
      augmenting_paths = self.find_augmenting_path()
      print(augmenting_paths)
      if not augmenting_paths:
        break
      self.matching_union(augmenting_paths)


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
      print(unmatched_V)
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
      # print(v)
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
          # Vamos iterar ao longo do caminho aumentante, alternando entre adicionar e remover arestas
          for i in range(len(path) - 1):
              u = path[i]
              v = path[i + 1]
              edge = (u, v) if u in self.graph.U else (v, u)
              print(edge)
              if edge in self.matching:
                  # Se a aresta já está no matching, removemos ela
                  self.matching.remove(edge)
              else:
                  # Caso contrário, adicionamos ela ao matching
                  self.matching.add(edge)

      return self.matching

