# About Graph Theory:

This repository contains a Python implementation of the famous **adjacency matrix** and **Graph Ploting** using the `Graph Theory` (Discrete Mathematics). The implementation includes generating an **adjacency matrix** for any given graph, which is represented by a set of vertices and edges.

## Table of Contents
- [Introduction](#introduction)
- [Graph Representation](#graph-representation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Example](#example)
- [Output Format](#output-format)
- [Contact](#contact)

## Introduction
An Adjacency Matrix is a square matrix used to represent a graph, where:
- Rows and columns represent vertices (nodes) of the graph.
- Entries (elements) in the matrix indicate edge connections between vertices.

## Graph Representation

The graph is represented using Python's `namedtuple` for defining the vertices and edges. Here's how the Konigsberg bridge problem is modeled:
```python
Graph = namedtuple('Graph', ['vertices', 'edges'])

vertices = ['A', 'B', 'C', 'D']
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")
]

G = Graph(vertices=vertices, edges=edges)
```

## Usage

1) Clone the repository:
```python
git clone https://github.com/yourusername/konigsberg-graph.git
```

2) Run the Python script to generate the adjacency matrix:
```python
python graph.py
```

## Dependencies
Libraries: 1) collections 2) tabulate

You can install libraries via pip if needed:
```python
pip install tabulate
```
```python
pip install collections
```

## Example
Here's an example adjacency matrix for the Konigsberg graph:
```
vertices = ['A', 'B', 'C', 'D']
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")
]

G = Graph(vertices=vertices, edges=edges)
matrix = adjacency_matrix(G)

```

## Output Format
```
╒═══╤═══╤═══╤═══╕
│ 0 │ 2 │ 2 │ 1 │
├───┼───┼───┼───┤
│ 2 │ 0 │ 0 │ 1 │
├───┼───┼───┼───┤
│ 2 │ 0 │ 0 │ 1 │
├───┼───┼───┼───┤
│ 1 │ 1 │ 1 │ 0 │
╘═══╧═══╧═══╧═══╛
```

## Contact

If you have any questions or suggestions, feel free to reach out to me at [LinkedIn](https://www.linkedin.com/in/anshmnsoni/).

## Thankyou
