from graphtk.graph_init import namedtuple

class Graph:
    def __init__(self):
        pass
    
    def paths(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        result = {v: [] for v in vertices}

        def dfs(src, path, visited):
            result[src].append(path[:])
            for neighbor in G[src]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(neighbor, path, visited)
                    path.pop()
                    visited.remove(neighbor)

        for v in vertices:
            dfs(v, [v], {v})
        return result

    def trails(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        result = {v: [] for v in vertices}

        def dfs(path, used_edges):
            result[path[0]].append(path[:])
            last = path[-1]
            for neighbor in G[last]:
                edge = (last, neighbor) if is_directed else tuple(sorted((last, neighbor)))
                if edge not in used_edges:
                    used_edges.add(edge)
                    path.append(neighbor)
                    dfs(path, used_edges)
                    path.pop()
                    used_edges.remove(edge)

        for v in vertices:
            dfs([v], set())
        return result

    def cycle(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        result = {v: [] for v in vertices}

        def dfs(start, curr, path, visited):
            for neighbor in G[curr]:
                if neighbor == start and len(path) > 2:
                    result[start].append(path[:] + [start])
                elif neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(start, neighbor, path, visited)
                    path.pop()
                    visited.remove(neighbor)

        for v in vertices:
            dfs(v, v, [v], {v})
        return result

    def simplepath(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        result = {v: [] for v in vertices}

        def dfs(src, path, visited):
            result[src].append(path[:])
            for neighbor in G[src]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(neighbor, path, visited)
                    path.pop()
                    visited.remove(neighbor)

        for v in vertices:
            result[v] = []
            dfs(v, [v], {v})
        return result
    
    def is_path(self, edges: list, vertices: list, is_directed: bool, path: dict):
        G = namedtuple(edges, vertices, is_directed)
        for i in range(len(path)-1):
            if path[i+1] not in G[path[i]]:
                return False
        return True

    def is_trail(self, edges: list, vertices: list, is_directed: bool, trail: dict):
        G = namedtuple(edges, vertices, is_directed)
        used_edges = set()

        for i in range(len(trail)-1):
            u, v = trail[i], trail[i+1]
            if v not in G[u]:
                return False
            edge = (u, v) if is_directed else tuple(sorted((u,v)))
            if edge in used_edges:
                return False
            used_edges.add(edge)
        return True

    def is_cycle(self, edges: list, vertices: list, is_directed: bool, cycle: dict):
        if len(cycle) < 3:
            return False
        if cycle[0] != cycle[-1]:
            return False
        return self.istrail(edges, vertices, is_directed, cycle)

    def is_simplepath(self, edges: list, vertices: list, is_directed: bool, path: dict):
        if len(set(path)) != len(path):
            return False
        return self.is_path(edges, vertices, is_directed, path)

    def is_traversable(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        visited = set()

        def dfs(v):
            visited.add(v)
            for neighbor in G[v]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(vertices[0])
        return len(visited) == len(vertices)

    def is_euler(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        if not self.is_traversable(edges, vertices, is_directed):
            return False
        degrees = [len(G[v]) for v in vertices]
        odd = sum(d % 2 for d in degrees)
        return odd == 0 or odd == 2
    
    def is_hamilton(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        n = len(vertices)
        
        def backtrack(path, visited):
            if len(path) == n:   # visited all vertices
                return True
            last = path[-1]
            for neighbor in G[last]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    if backtrack(path, visited):
                        return True
                    path.pop()
                    visited.remove(neighbor)       
            return False

        for v in vertices:
            if backtrack([v], {v}):
                return True
        return False

    def is_complete(self, edges: list, vertices: list, is_directed: bool):
        n = len(vertices)
        expected_edges = n * (n-1) if is_directed else n * (n-1) // 2
        return len(edges) == expected_edges

    def is_regular(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        degrees = [len(G[v]) for v in vertices]
        return all(d == degrees[0] for d in degrees)

    def is_bipartite(self, edges: list, vertices: list, is_directed: bool):
        G = namedtuple(edges, vertices, is_directed)
        color = {}
        for v in vertices:
            if v not in color:
                color[v] = 0
                stack = [v]
                while stack:
                    u = stack.pop()
                    for neighbor in G[u]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[u]
                            stack.append(neighbor)
                        elif color[neighbor] == color[u]:
                            return False       
        return True

    def is_planner(self, edges: list, vertices: list, is_directed: bool):
        if is_directed:
            return False  # usually planar graph is defined for undirected
        n = len(vertices)
        m = len(edges)
        # Kuratowski's theorem is complex; simple bound:
        # For planar graphs: m ≤ 3n - 6 (for n ≥ 3)
        return m <= 3*n - 6
