"""
Tests for graphtk.toolkit.Toolkit — the public facade that delegates
to Graph, Matrices, GraphColoring, AdjacencyList, and Edge.

These are integration-style tests that verify the facade wires
through to the underlying implementations correctly.
"""


class TestToolkitGraphDelegation:
    """Toolkit forwards graph-theory calls to the Graph class."""

    def test_paths(self, toolkit, triangle_graph):
        edges, vertices, is_directed = triangle_graph
        result = toolkit.paths(edges, vertices, is_directed)
        assert isinstance(result, dict)
        assert set(result.keys()) == set(vertices)

    def test_is_traversable(self, toolkit, triangle_graph):
        edges, vertices, is_directed = triangle_graph
        assert toolkit.is_traversable(edges, vertices, is_directed) is True

    def test_is_bipartite(self, toolkit, bipartite_graph):
        edges, vertices, is_directed = bipartite_graph
        assert toolkit.is_bipartite(edges, vertices, is_directed) is True

    def test_is_complete(self, toolkit, complete_k4_graph):
        edges, vertices, is_directed = complete_k4_graph
        assert toolkit.is_complete(edges, vertices, is_directed) is True

    def test_is_euler(self, toolkit, triangle_graph):
        edges, vertices, is_directed = triangle_graph
        assert toolkit.is_euler(edges, vertices, is_directed) is True


class TestToolkitMatrixDelegation:
    """Toolkit forwards matrix calls to the Matrices class."""

    def test_adjacency_matrix(self, toolkit, directed_triangle):
        edges, vertices, is_directed = directed_triangle
        adj = toolkit.adjacency_matrix(edges, vertices, is_directed)
        assert len(adj) == len(vertices)

    def test_weight_matrix(self, toolkit, directed_linear):
        edges, vertices, is_directed = directed_linear
        w = toolkit.weight_matrix(edges, vertices, is_directed)
        assert len(w) == len(vertices)


class TestToolkitColoringDelegation:
    """Toolkit forwards coloring calls to GraphColoring."""

    def test_vertex_coloring(self, toolkit, triangle_graph):
        edges, vertices, _ = triangle_graph
        result = toolkit.vertex_coloring(edges, vertices)
        assert isinstance(result, dict)
        assert set(result.keys()) == set(vertices)


class TestToolkitAdjacencyListDelegation:
    """Toolkit forwards adjacency-list calls to AdjacencyList."""

    def test_adjacency_list(self, toolkit, triangle_graph):
        edges, vertices, is_directed = triangle_graph
        result = toolkit.adjacency_list(edges, vertices, is_directed)
        assert isinstance(result, dict)
        assert set(result.keys()) == set(vertices)
