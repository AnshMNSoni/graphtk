"""
Tests for graphtk.graphs.Graph — paths, trails, cycles, traversal checks,
Euler / Hamilton properties, bipartiteness, regularity, completeness, planarity.
"""

import pytest


# ═══════════════════════════════════════════════════════════════════
#  Paths
# ═══════════════════════════════════════════════════════════════════


class TestPaths:
    """Graph.paths() — enumerate all DFS-based paths from each vertex."""

    def test_triangle_paths_include_all_vertices(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act
        result = graph.paths(edges, vertices, is_directed)

        # Assert — every vertex has at least itself as a trivial path
        for v in vertices:
            assert any(v in p for p in result[v])

    def test_linear_graph_paths(self, graph, linear_graph):
        # Arrange
        edges, vertices, is_directed = linear_graph

        # Act
        result = graph.paths(edges, vertices, is_directed)

        # Assert — A can reach D via the full path
        paths_from_a = result["A"]
        assert any("D" in p for p in paths_from_a)

    def test_single_node_returns_self(self, graph, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act
        result = graph.paths(edges, vertices, is_directed)

        # Assert
        assert result["A"] == [["A"]]


# ═══════════════════════════════════════════════════════════════════
#  Trails
# ═══════════════════════════════════════════════════════════════════


class TestTrails:
    """Graph.trails() — every edge used at most once."""

    def test_triangle_trails(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act
        result = graph.trails(edges, vertices, is_directed)

        # Assert — each starting vertex should produce multiple trails
        for v in vertices:
            assert len(result[v]) >= 1

    def test_single_node_trail(self, graph, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act
        result = graph.trails(edges, vertices, is_directed)

        # Assert
        assert result["A"] == [["A"]]


# ═══════════════════════════════════════════════════════════════════
#  Cycles
# ═══════════════════════════════════════════════════════════════════


class TestCycle:
    """Graph.cycle() — finds cycles that return to the starting vertex."""

    def test_triangle_has_cycle(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act
        result = graph.cycle(edges, vertices, is_directed)

        # Assert — at least one vertex must have a cycle
        has_cycle = any(len(result[v]) > 0 for v in vertices)
        assert has_cycle

    def test_linear_graph_no_cycle(self, graph, linear_graph):
        # Arrange
        edges, vertices, is_directed = linear_graph

        # Act
        result = graph.cycle(edges, vertices, is_directed)

        # Assert — linear graphs cannot have cycles
        for v in vertices:
            assert result[v] == []

    def test_single_node_no_cycle(self, graph, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act
        result = graph.cycle(edges, vertices, is_directed)

        # Assert
        assert result["A"] == []


# ═══════════════════════════════════════════════════════════════════
#  Simple Paths
# ═══════════════════════════════════════════════════════════════════


class TestSimplePath:
    """Graph.simplepath() — no repeated vertices."""

    def test_triangle_simple_paths(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act
        result = graph.simplepath(edges, vertices, is_directed)

        # Assert — every path has no duplicate vertices
        for v in vertices:
            for path in result[v]:
                assert len(path) == len(set(path))

    def test_single_node_simple_path(self, graph, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act
        result = graph.simplepath(edges, vertices, is_directed)

        # Assert
        assert result["A"] == [["A"]]


# ═══════════════════════════════════════════════════════════════════
#  is_path / is_trail / is_simplepath
# ═══════════════════════════════════════════════════════════════════


class TestIsPath:
    """Graph.is_path() — validate a sequence of vertices as a walk."""

    def test_valid_path(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_path(edges, vertices, is_directed, ["A", "B", "C"]) is True

    def test_invalid_path(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert — no direct edge A→D
        assert graph.is_path(edges, vertices, is_directed, ["A", "D"]) is False


class TestIsTrail:
    """Graph.is_trail() — path using each edge at most once."""

    def test_valid_trail(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_trail(edges, vertices, is_directed, ["A", "B", "C"]) is True

    def test_invalid_trail_repeated_edge(self, graph):
        # Arrange — square with extra traversal repeating an edge
        edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
        vertices = ["A", "B", "C", "D"]

        # Act / Assert — trail A→B→A uses edge A-B twice
        assert graph.is_trail(edges, vertices, False, ["A", "B", "A"]) is False


class TestIsSimplePath:
    """Graph.is_simplepath() — walk with no repeated vertices."""

    def test_valid_simple_path(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_simplepath(edges, vertices, is_directed, ["A", "B", "C"]) is True

    def test_invalid_simple_path_repeated_vertex(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert — vertex A repeated
        assert graph.is_simplepath(edges, vertices, is_directed, ["A", "B", "A"]) is False


# ═══════════════════════════════════════════════════════════════════
#  Traversability
# ═══════════════════════════════════════════════════════════════════


class TestIsTraversable:
    """Graph.is_traversable() — connected graph check via DFS."""

    def test_connected_graph(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_traversable(edges, vertices, is_directed) is True

    def test_disconnected_graph(self, graph, disconnected_graph):
        # Arrange
        edges, vertices, is_directed = disconnected_graph

        # Act / Assert
        assert graph.is_traversable(edges, vertices, is_directed) is False


# ═══════════════════════════════════════════════════════════════════
#  Euler
# ═══════════════════════════════════════════════════════════════════


class TestIsEuler:
    """Graph.is_euler() — Eulerian path / circuit existence."""

    def test_triangle_is_euler(self, graph, triangle_graph):
        # Arrange — all vertices have even degree (2)
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_euler(edges, vertices, is_directed) is True

    def test_linear_graph_is_euler(self, graph, linear_graph):
        # Arrange — exactly 2 vertices of odd degree
        edges, vertices, is_directed = linear_graph

        # Act / Assert
        assert graph.is_euler(edges, vertices, is_directed) is True

    def test_disconnected_not_euler(self, graph, disconnected_graph):
        # Arrange
        edges, vertices, is_directed = disconnected_graph

        # Act / Assert
        assert graph.is_euler(edges, vertices, is_directed) is False


# ═══════════════════════════════════════════════════════════════════
#  Hamilton
# ═══════════════════════════════════════════════════════════════════


class TestIsHamilton:
    """Graph.is_hamilton() — Hamiltonian path existence."""

    def test_triangle_has_hamiltonian_path(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_hamilton(edges, vertices, is_directed) is True

    def test_linear_has_hamiltonian_path(self, graph, linear_graph):
        # Arrange
        edges, vertices, is_directed = linear_graph

        # Act / Assert
        assert graph.is_hamilton(edges, vertices, is_directed) is True


# ═══════════════════════════════════════════════════════════════════
#  Complete / Regular / Bipartite / Planar
# ═══════════════════════════════════════════════════════════════════


class TestIsComplete:
    """Graph.is_complete() — edge-count verification."""

    def test_k4_is_complete(self, graph, complete_k4_graph):
        # Arrange
        edges, vertices, is_directed = complete_k4_graph

        # Act / Assert
        assert graph.is_complete(edges, vertices, is_directed) is True

    def test_triangle_is_complete(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_complete(edges, vertices, is_directed) is True

    def test_linear_is_not_complete(self, graph, linear_graph):
        # Arrange
        edges, vertices, is_directed = linear_graph

        # Act / Assert
        assert graph.is_complete(edges, vertices, is_directed) is False


class TestIsRegular:
    """Graph.is_regular() — all vertices have the same degree."""

    def test_triangle_is_regular(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_regular(edges, vertices, is_directed) is True

    def test_linear_is_not_regular(self, graph, linear_graph):
        # Arrange — endpoints have degree 1, middle nodes have degree 2
        edges, vertices, is_directed = linear_graph

        # Act / Assert
        assert graph.is_regular(edges, vertices, is_directed) is False


class TestIsBipartite:
    """Graph.is_bipartite() — two-colorability check."""

    def test_bipartite_graph(self, graph, bipartite_graph):
        # Arrange
        edges, vertices, is_directed = bipartite_graph

        # Act / Assert
        assert graph.is_bipartite(edges, vertices, is_directed) is True

    def test_non_bipartite_graph(self, graph, non_bipartite_graph):
        # Arrange — triangle (odd cycle)
        edges, vertices, is_directed = non_bipartite_graph

        # Act / Assert
        assert graph.is_bipartite(edges, vertices, is_directed) is False

    def test_single_node_is_bipartite(self, graph, single_node_graph):
        # Arrange
        edges, vertices, is_directed = single_node_graph

        # Act / Assert
        assert graph.is_bipartite(edges, vertices, is_directed) is True

    def test_square_is_bipartite(self, graph, square_graph):
        # Arrange — even cycle
        edges, vertices, is_directed = square_graph

        # Act / Assert
        assert graph.is_bipartite(edges, vertices, is_directed) is True


class TestIsPlanner:
    """Graph.is_planner() — Kuratowski bound for planarity."""

    def test_triangle_is_planar(self, graph, triangle_graph):
        # Arrange
        edges, vertices, is_directed = triangle_graph

        # Act / Assert
        assert graph.is_planner(edges, vertices, is_directed) is True

    def test_directed_returns_false(self, graph, directed_triangle):
        # Arrange
        edges, vertices, is_directed = directed_triangle

        # Act / Assert
        assert graph.is_planner(edges, vertices, is_directed) is False
