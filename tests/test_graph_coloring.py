"""
Tests for graphtk.graph_coloring.GraphColoring — greedy vertex coloring.
"""


class TestVertexColoring:
    """GraphColoring.vertex_coloring() — greedy chromatic assignment."""

    def test_triangle_uses_three_colors(self, coloring, triangle_graph):
        # Arrange
        edges, vertices, _ = triangle_graph

        # Act
        result = coloring.vertex_coloring(edges, vertices)

        # Assert — triangle needs exactly 3 colors
        assert len(set(result.values())) == 3

    def test_bipartite_uses_two_colors(self, coloring, bipartite_graph):
        # Arrange
        edges, vertices, _ = bipartite_graph

        # Act
        result = coloring.vertex_coloring(edges, vertices)

        # Assert — bipartite ⇒ at most 2 colors
        assert len(set(result.values())) <= 2

    def test_single_node_one_color(self, coloring, single_node_graph):
        # Arrange
        edges, vertices, _ = single_node_graph

        # Act
        result = coloring.vertex_coloring(edges, vertices)

        # Assert
        assert result == {"A": 0}

    def test_no_adjacent_same_color(self, coloring, complete_k4_graph):
        # Arrange
        edges, vertices, _ = complete_k4_graph

        # Act
        result = coloring.vertex_coloring(edges, vertices)

        # Assert — no two adjacent vertices share the same color
        for u, v in edges:
            assert result[u] != result[v]
