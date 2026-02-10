"""
Tests for graphtk.adjacency_list.AdjacencyList — build adjacency list
with edge multiplicities.
"""


class TestAdjacencyList:
    """AdjacencyList.adjacency_list() — neighbor counts per vertex."""

    def test_triangle_undirected(self, adjacency_list, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act
        result = adjacency_list.adjacency_list(edges, vertices, is_directed)

        # Assert — each vertex has exactly 2 neighbours with count 1
        for v in vertices:
            assert len(result[v]) == 2
            for _, count in result[v]:
                assert count == 1

    def test_directed_linear(self, adjacency_list, directed_linear):
        # Arrange
        edges, vertices, is_directed = directed_linear

        # Act
        result = adjacency_list.adjacency_list(edges, vertices, is_directed)

        # Assert  A → B, B → C
        neighbors_a = {n: c for n, c in result["A"]}
        assert "B" in neighbors_a
        assert "C" not in neighbors_a

    def test_no_edges(self, adjacency_list, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act
        result = adjacency_list.adjacency_list(edges, vertices, is_directed)

        # Assert
        assert result["A"] == []

    def test_multi_edge_counts(self, adjacency_list):
        # Arrange — duplicate edges (multi-graph)
        edges = [("A", "B"), ("A", "B")]
        vertices = ["A", "B"]

        # Act
        result = adjacency_list.adjacency_list(edges, vertices, is_directed=False)

        # Assert — B should appear with count 2 in A's list
        neighbors_a = dict(result["A"])
        assert neighbors_a["B"] == 2
