# to map graph vertices and edges

def namedtuple(edges: list, vertices: list, is_directed: bool):
    adj = {v: [] for v in vertices}
    for v1, v2 in edges:
        adj[v1].append(v2)
        if not is_directed:
            adj[v2].append(v1)
    return adj
