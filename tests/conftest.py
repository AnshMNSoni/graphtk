"""
Shared pytest fixtures for graphtk test suite.

Fixtures provide reusable graph data (vertices, edges) so individual
tests stay focused on behaviour, not setup boilerplate.
"""

import pytest

from graphtk.graphs import Graph
from graphtk.matrix import Matrices
from graphtk.graph_coloring import GraphColoring
from graphtk.adjacency_list import AdjacencyList
from graphtk.toolkit import Toolkit


# ── Class instances ──────────────────────────────────────────────


@pytest.fixture
def graph():
    """Return a fresh Graph instance."""
    return Graph()


@pytest.fixture
def matrices():
    """Return a fresh Matrices instance."""
    return Matrices()


@pytest.fixture
def coloring():
    """Return a fresh GraphColoring instance."""
    return GraphColoring()


@pytest.fixture
def adjacency_list():
    """Return a fresh AdjacencyList instance."""
    return AdjacencyList()


@pytest.fixture
def toolkit():
    """Return a fresh Toolkit instance (facade)."""
    return Toolkit()


# ── Undirected graph fixtures ────────────────────────────────────


@pytest.fixture
def triangle_graph():
    """
    Triangle graph: A — B — C — A

        A
       / \
      B — C
    """
    vertices = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("A", "C")]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def linear_graph():
    """
    Linear (path) graph: A — B — C — D
    """
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("B", "C"), ("C", "D")]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def single_node_graph():
    """
    Isolated single-node graph with no edges.
    """
    vertices = ["A"]
    edges = []
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def disconnected_graph():
    """
    Two disconnected components: A — B   and   C — D
    """
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("C", "D")]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def square_graph():
    """
    Square (cycle-4) graph: A — B — C — D — A
    """
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def complete_k4_graph():
    """
    Complete graph K4 (undirected) on vertices 1..4.
    """
    vertices = [1, 2, 3, 4]
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4),
        (3, 4),
    ]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def bipartite_graph():
    """
    Bipartite graph:  {A, B} <-> {C, D}
    """
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "C"), ("A", "D"), ("B", "C"), ("B", "D")]
    is_directed = False
    return edges, vertices, is_directed


@pytest.fixture
def non_bipartite_graph():
    """
    Odd-cycle graph (triangle) — NOT bipartite.
    """
    vertices = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("A", "C")]
    is_directed = False
    return edges, vertices, is_directed


# ── Directed graph fixtures ──────────────────────────────────────


@pytest.fixture
def directed_triangle():
    """
    Directed triangle: A → B → C → A
    """
    vertices = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    is_directed = True
    return edges, vertices, is_directed


@pytest.fixture
def directed_linear():
    """
    Directed path: A → B → C
    """
    vertices = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    is_directed = True
    return edges, vertices, is_directed
