"""
Graph class for MST

Madeline Porcaro
"""

class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.node = []
        self.MinST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.node.append(value)
    
    def printSolution(self, s, d, w):
        for s, d, w in self.MinST:
            print(f'{s} - {d} : {w}')