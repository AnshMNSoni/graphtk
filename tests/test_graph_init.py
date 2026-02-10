"""
Tests for graphtk.graph_init — the namedtuple adjacency-list builder.
"""

from graphtk.graph_init import namedtuple


class TestNamedtupleUndirected:
    """Build undirected adjacency lists."""

    def test_single_edge(self):
        # Arrange
        edges = [("A", "B")]
        vertices = ["A", "B"]

        # Act
        adj = namedtuple(edges, vertices, is_directed=False)

        # Assert
        assert "B" in adj["A"]
        assert "A" in adj["B"]

    def test_triangle(self):
        # Arrange
        edges = [("A", "B"), ("B", "C"), ("A", "C")]
        vertices = ["A", "B", "C"]

        # Act
        adj = namedtuple(edges, vertices, is_directed=False)

        # Assert
        assert set(adj["A"]) == {"B", "C"}
        assert set(adj["B"]) == {"A", "C"}
        assert set(adj["C"]) == {"B", "A"}

    def test_no_edges(self):
        # Arrange
        vertices = ["X", "Y"]

        # Act
        adj = namedtuple([], vertices, is_directed=False)

        # Assert
        assert adj["X"] == []
        assert adj["Y"] == []


class TestNamedtupleDirected:
    """Build directed adjacency lists."""

    def test_single_directed_edge(self):
        # Arrange
        edges = [("A", "B")]
        vertices = ["A", "B"]

        # Act
        adj = namedtuple(edges, vertices, is_directed=True)

        # Assert
        assert "B" in adj["A"]
        assert "A" not in adj["B"]

    def test_cycle_directed(self):
        # Arrange
        edges = [("A", "B"), ("B", "C"), ("C", "A")]
        vertices = ["A", "B", "C"]

        # Act
        adj = namedtuple(edges, vertices, is_directed=True)

        # Assert
        assert adj["A"] == ["B"]
        assert adj["B"] == ["C"]
        assert adj["C"] == ["A"]
