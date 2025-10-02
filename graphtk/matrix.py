import math

class Matrices:
    def __init__(self):
        pass    
    
    def multiply_matrices(self, A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])

        if cols_A != rows_B:
            raise ValueError("Number of columns of A must equal number of rows of B")

        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):  
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def adjacency_matrix(self, edges: list, vertices: list, is_directed: bool):
        try:
            G = {vertex: [] for vertex in vertices}

            for edge in edges:
                vertex1, vertex2 = edge[0], edge[1]
                G[vertex1].append(vertex2)

                if not is_directed:
                    BaseExceptionGroup[vertex2].append(vertex1)

            length = len(vertices)
            adj_matrix = [[0]*length for _ in range(length)]

            for i in range(length):
                for j in range(length):
                    cnt = G[vertices[i]].count(vertices[j])
                    adj_matrix[i][j] = cnt
            return adj_matrix

        except Exception as e:
            print(f"Error: {e}")
            return None

    def weight_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        try:
            weight_matrix = self.adjacency_matrix(edges, vertices, True)

            n = len(vertices)
            for i in range(n):
                for j in range(n):
                    if i != j and weight_matrix[i][j] == 0:
                        weight_matrix[i][j] = math.inf

            # Floyd-Warshall algorithm
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        weight_matrix[i][j] = min(weight_matrix[i][j], weight_matrix[i][k] + weight_matrix[k][j])

            # convert unreachable paths back to 0
            for i in range(n):
                for j in range(n):
                    if weight_matrix[i][j] == math.inf:
                        weight_matrix[i][j] = 0
            return weight_matrix

        except Exception as e:
            print(f"Error: {e}")
            return None

    def b_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        adj = self.adjacency_matrix(edges, vertices, True)
        B_matrix = [[adj[i][j] for j in range(len(vertices))] for i in range(len(vertices))]
        A = [[adj[i][j] for j in range(len(vertices))] for i in range(len(vertices))]

        for _ in range(len(vertices)-1):
            C = self.multiply_matrices(A, adj)

            for i in range(len(vertices)):
                for j in range(len(vertices)):
                    B_matrix[i][j] += C[i][j]

            # Update A = C (element by element, not by reference)
            A = [[C[i][j] for j in range(len(vertices))] for i in range(len(vertices))]
        return B_matrix

    
    def path_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        path_matrix = self.b_matrix(edges, vertices)
        for _ in range(len(vertices)-1):
            A = path_matrix
            B = path_matrix
            C = self.multiply_matrices(A, B)
            
            for i in range(len(vertices)):
                for j in range(len(vertices)):
                    path_matrix[i][j] = path_matrix[i][j] + C[i][j]
            A = C
            
        for i in range(len(vertices)):
                    for j in range(len(vertices)):
                        if(path_matrix[i][j]!=0):
                            path_matrix[i][j] = 1
        return path_matrix
