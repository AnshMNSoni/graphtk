# Directed and Undirected Edges

class Edge:
    def __init__(self):
        pass
    
    def edges(self, vertices: list, is_directed: bool):
        cnt = 0
        edge = []

        for i in vertices:
            for j in range(cnt, len(vertices)):
                num = int(input(f"Enter the number of edges between {i}-{vertices[j]}: "))

                for _ in range(num):  # handling self loops
                    edge.append((i, vertices[j]))

            # if undirected, avoid duplicate edges
            if not is_directed:
                cnt += 1
        return edge
