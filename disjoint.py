"""
Disjoint Class for MST

Madeline Porcaro
"""

class Disjoint:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    # recursive seraching function
    def find(self, obj):
        if self.parent[obj] == obj:
            return obj
        else:
            return self.find(self.parent[obj])

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)

        if self.rank[aroot] < self.rank[broot]:
            self.parent[aroot] = broot
        elif self.rank[aroot] > self.rank[broot]:
             self.parent[broot] = aroot
        else:
             self.parent[aroot] = broot
             self.rank[aroot] += 1