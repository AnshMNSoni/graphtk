# Graph Theory Toolkit (GraphTK):

## Table of Contents
- [Introduction](#introduction)
- [Basic Terminologies](#basic-terminologies)
- [Usage](#usage)
- [Syntax and Methods](#syntax-and-methods)
- [Contact](#-connect-with-me)

## Introduction 
This library provides a comprehensive Python implementation of core **Graph Theory** concepts from **Discrete Mathematics**. It allows you to create and analyze graphs represented by vertices and edges, with functionalities including generating **adjacency matrices**, **path matrices**, **weight matrices**, performing **graph coloring**, and more. With this toolkit, you can easily explore, and manipulate various graph structures in a simple and intuitive way.

## Basic Terminologies
- **Graph** → A collection of vertices (nodes) connected by edges (links).
- **Adjacency Matrix** → A square matrix showing which vertices are connected by an edge.
- **Incidence Matrix** → A matrix showing the relation between vertices and edges.
- **Path Matrix (Connectivity Matrix)** → A matrix that indicates whether a path exists between any two vertices.
- **Weight Matrix (Cost Matrix)** → A matrix showing edge weights (like distances or costs) between vertices.
- **Path** → A sequence of vertices connected by edges (edges may or may not repeat).
- **Simple Path** → A path where no vertex (and hence no edge) is repeated.
- **Trail** → A walk where edges are not repeated, but vertices may repeat.
- **Cycle (or Circuit)** → A closed path where the start and end vertices are the same, with no repetition of edges/vertices (except start = end).
- **Euler Path** → A path that uses every edge exactly once.
- **Euler Circuit (Euler Graph)** → A cycle that uses every edge exactly once and returns to the starting vertex.
- **Hamiltonian Path** → A path that visits every vertex exactly once.
- **Hamiltonian Cycle** → A cycle that visits every vertex exactly once and returns to the start.
- **Connected Graph** → A graph where there’s a path between every pair of vertices.
- **Complete Graph** → A graph where every pair of vertices is connected by an edge.
- **Bipartite Graph** → A graph whose vertices can be split into two disjoint sets with edges only across sets.
- **Tree** → A connected graph with no cycles.
- **Spanning Tree** → A subgraph that connects all vertices with minimum edges and no cycles.

## Usage

open command prompt and run:
```python
pip install graphtk
```

## Syntax and Methods
1️⃣ Input Format: Vertices and Edges
```
vertices = ['A', 'B', 'C', 'D'] # list

# list of tuples
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")
]
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = tk.edges(vertices, True) # You can also provide your own edges; just ensure they follow the correct format.
print(edges)
```

2️⃣ Adjacency Matrix, Path Matrix, Weight Matrix, B-Matrix
- Syntax
```
# adjacency matrix
adjacency_matrix(edges: list, vertices: list, is_directed: bool)

# weight matrix
weight_matrix(edges: list, vertices: list, is_directed: bool = None)

# path matrix
path_matrix(edges: list, vertices: list, is_directed: bool = None)

# B-matrix
b_matrix(edges: list, vertices: list, is_directed: bool = None)
```
- Implementation 
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

# adjacency matrix
matrix = tk.adjacency_matrix(edges, vertices, True)
print(matrix)

# path matrix
matrix = tk.path_matrix(edges, vertices)

# weight matrix
matrix = tk.weight_matrix(edges, vertices)

# B-matrix
matrix = tk.b_matrix(edges, vertices)
```

3️⃣ Graph Terminologies<br/>
➡️ Paths
- Syntax
```
paths(edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.paths(edges, vertices, True)
print(result)
```

➡️ trails 
- Syntax
```
trails(edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.trails(edges, vertices, True)
print(result)
```
➡️ cycle
- Syntax
```
cycle(edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.cycle(edges, vertices, True)
print(result)
```
➡️ simplepath
- Syntax
```
simplepath(edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.simplepath(edges, vertices, True)
print(result)
```
➡️ adjacency_list
- Syntax
```
adjacency_list(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.adjacency_list(edges, vertices, True)
print(result)
```
➡️ is_path
- Syntax
```
is_path(edges: list, vertices: list, is_directed: bool, path: dict)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_path(edges, vertices, True, {'A': [['A'], ['C', 'A']]})
print(result)
```
➡️ is_trail
- Syntax
```
is_trail(self, edges: list, vertices: list, is_directed: bool, trail: dict)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_trail(edges, vertices, True, {'A': [['A'], ['C', 'A']]})
print(result)
```
➡️ is_cycle
- Syntax
```
is_cycle(self, edges: list, vertices: list, is_directed: bool, cycle: dict)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_cycle(edges, vertices, True, {'A': [['A'], ['C', 'A']]})
print(result)
```
➡️ is_simplepath
- Syntax
```
is_simplepath(self, edges: list, vertices: list, is_directed: bool, path: dict)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_simplepath(edges, vertices, True, {'A': [['A'], ['C', 'A']]})
print(result)
```
➡️ is_traversable
- Syntax
```
is_traversable(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_traversable(edges, vertices, True)
print(result)
```
➡️ is_euler
- Syntax
```
is_euler(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_euler(edges, vertices, True)
print(result)
```
➡️ is_hamilton
- Syntax
```
is_hamilton(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_hamilton(edges, vertices, True)
print(result)
```
➡️ is_complete
- Syntax
```
is_complete(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_complete(edges, vertices, True)
print(result)
```
➡️ is_regular
- Syntax
```
is_regular(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_regular(edges, vertices, True)
print(result)
```
➡️ is_bipartite
- Syntax
```
is_bipartite(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_bipartite(edges, vertices, True)
print(result)
```
➡️ is_planner
- Syntax
```
is_planner(self, edges: list, vertices: list, is_directed: bool)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.is_planner(edges, vertices, True)
print(result)
```
➡️ vertex_coloring
- Syntax
```
vertex_coloring(self, edges: list, vertices: list, is_directed: bool = None)
```
- Implementation
```
from graphtk.toolkit import Toolkit

tk = Toolkit()

vertices = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('C', 'A')]

result = tk.vertex_coloring(edges, vertices)
print(result)
```

## 📢 Connect with Me
If you found this project helpful or have any suggestions, feel free to connect:

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-anshmnsoni-0077B5.svg?logo=linkedin)](https://www.linkedin.com/in/anshmnsoni)  
- [![GitHub](https://img.shields.io/badge/GitHub-AnshMNSoni-181717.svg?logo=github)](https://github.com/AnshMNSoni)
- [![Reddit](https://img.shields.io/badge/Reddit-u/AnshMNSoni-FF4500.svg?logo=reddit)](https://www.reddit.com/user/AnshMNSoni)

### Thankyou 💫 
