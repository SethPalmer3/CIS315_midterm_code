"""
Krusakl's Algorithm

I added classes here because I kinda realized it's
more efficent

unrelated note: I cried from laughing at my own stupidty
and also because this algorithms class gives me pain

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


    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            self.printSolution(u, v, weight)

g = Graph(5)
g.addEdge(0, 1, 8)
g.addEdge(0, 2, 5)
g.addEdge(1, 2, 9)
g.addEdge(1, 3, 11)
g.addEdge(2, 3, 15)
g.addEdge(2, 4, 10)
g.addEdge(3, 4, 7)
g.kruskal()