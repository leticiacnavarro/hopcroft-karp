class BipartiteGraph:
    def __init__(self, U, V, edges):
        """
        Inicializa o grafo bipartido com dois conjuntos de vértices U e V, e um conjunto de arestas.

        :param U: Conjunto de vértices U (lado esquerdo do grafo bipartido).
        :param V: Conjunto de vértices V (lado direito do grafo bipartido).
        :param edges: Lista de arestas, onde cada aresta é representada por uma tupla (u, v) com u em U e v em V.
        """
        self.U = set(U)
        self.V = set(V)
        self.edges = set(edges)

    def add_edge(self, u, v):
        """
        Adiciona uma aresta entre um vértice u em U e um vértice v em V.

        :param u: Vértice do conjunto U.
        :param v: Vértice do conjunto V.
        """
        if u in self.U and v in self.V:
            self.edges.add((u, v))
        else:
            raise ValueError("A aresta deve conectar um vértice de U com um vértice de V.")

    def remove_edge(self, u, v):
        """
        Remove a aresta entre o vértice u e o vértice v, se existir.

        :param u: Vértice do conjunto U.
        :param v: Vértice do conjunto V.
        """
        self.edges.discard((u, v))

    def neighbors_U(self, u):
        """
        Retorna os vizinhos de um vértice u em U (os vértices de V conectados a u).

        :param u: Vértice do conjunto U.
        :return: Conjunto de vértices em V que são vizinhos de u.
        """
        return {v for (x, v) in self.edges if x == u}

    def neighbors_V(self, v):
        """
        Retorna os vizinhos de um vértice v em V (os vértices de U conectados a v).

        :param v: Vértice do conjunto V.
        :return: Conjunto de vértices em U que são vizinhos de v.
        """
        return {u for (u, x) in self.edges if x == v}

    def __repr__(self):
        return f"BipartiteGraph(U={self.U}, V={self.V}, edges={self.edges})"
