"""
Tests for graphtk.matrix.Matrices — adjacency matrix, weight matrix,
B-matrix, path matrix, and helper multiply_matrices.
"""

import math


class TestMultiplyMatrices:
    """Matrices.multiply_matrices() — standard matrix multiplication."""

    def test_identity_multiplication(self, matrices):
        # Arrange
        A = [[1, 0], [0, 1]]
        B = [[5, 3], [2, 7]]

        # Act
        result = matrices.multiply_matrices(A, B)

        # Assert
        assert result == [[5, 3], [2, 7]]

    def test_2x2_multiplication(self, matrices):
        # Arrange
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        # Act
        result = matrices.multiply_matrices(A, B)

        # Assert
        assert result == [[19, 22], [43, 50]]

    def test_incompatible_dimensions_raises(self, matrices):
        # Arrange
        A = [[1, 2, 3]]
        B = [[1], [2]]

        # Act / Assert
        import pytest
        with pytest.raises(ValueError, match="columns"):
            matrices.multiply_matrices(A, B)


class TestAdjacencyMatrix:
    """Matrices.adjacency_matrix() — build adj matrix from edge list."""

    def test_directed_triangle(self, matrices, directed_triangle):
        # Arrange
        edges, vertices, is_directed = directed_triangle

        # Act
        adj = matrices.adjacency_matrix(edges, vertices, is_directed)

        # Assert — A→B, B→C, C→A
        idx = {v: i for i, v in enumerate(vertices)}
        assert adj[idx["A"]][idx["B"]] == 1
        assert adj[idx["B"]][idx["C"]] == 1
        assert adj[idx["C"]][idx["A"]] == 1
        # No reverse edges
        assert adj[idx["B"]][idx["A"]] == 0

    def test_no_edges(self, matrices):
        # Arrange
        vertices = ["X", "Y"]

        # Act
        adj = matrices.adjacency_matrix([], vertices, True)

        # Assert
        assert adj == [[0, 0], [0, 0]]


class TestWeightMatrix:
    """Matrices.weight_matrix() — shortest path distances (Floyd-Warshall)."""

    def test_directed_linear_shortest_distances(self, matrices, directed_linear):
        # Arrange
        edges, vertices, is_directed = directed_linear

        # Act
        w = matrices.weight_matrix(edges, vertices, is_directed)

        # Assert — A→B = 1, A→C = 2, B→C = 1
        idx = {v: i for i, v in enumerate(vertices)}
        assert w[idx["A"]][idx["B"]] == 1
        assert w[idx["A"]][idx["C"]] == 2
        assert w[idx["B"]][idx["C"]] == 1


class TestBMatrix:
    """Matrices.b_matrix() — reachability-count matrix."""

    def test_directed_triangle_b_matrix(self, matrices, directed_triangle):
        # Arrange
        edges, vertices, is_directed = directed_triangle

        # Act
        b = matrices.b_matrix(edges, vertices, is_directed)

        # Assert — result should be a square matrix
        assert len(b) == len(vertices)
        assert all(len(row) == len(vertices) for row in b)


class TestPathMatrix:
    """Matrices.path_matrix() — binary reachability matrix."""

    def test_directed_triangle_path_matrix(self, matrices, directed_triangle):
        # Arrange
        edges, vertices, is_directed = directed_triangle

        # Act
        pm = matrices.path_matrix(edges, vertices, is_directed)

        # Assert — all entries are 0 or 1
        for row in pm:
            for val in row:
                assert val in (0, 1)
