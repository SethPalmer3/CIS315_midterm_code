"""
Graph class for MST

Madeline Porcaro
"""

class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

     # recursive seraching function
    def find(self, parent, obj):
        if parent[obj] == obj:
            return obj
        else:
            return self.find(parent, parent[obj])

    def union(self, parent, rank, a, b):
        aroot = self.find(parent, a)
        broot = self.find(parent, b)

        if rank[aroot] < rank[broot]:
            parent[aroot] = broot
        elif rank[aroot] > rank[broot]:
            parent[broot] = aroot
        else:
            parent[aroot] = broot
            rank[aroot] += 1
    
    def printSolution(self, s, d, w):
        for s, d, w in self.graph:
            print(f'{s} - {d} : {w}')