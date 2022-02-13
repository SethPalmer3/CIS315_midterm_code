"""
Bellman-Ford

Madeline Porcaro
"""
class Graph:
    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])

    # Print the solution
    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for k in range(self.V):
            print(f'{distance} : {distance[k]}')

    def bellman_ford(self, src):
        distance = [float("Inf")] * self.V
        distance[src] = 0
        for i in range(self.V - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c

        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(distance)



g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 3)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, -5)
g.bellman_ford(0)
