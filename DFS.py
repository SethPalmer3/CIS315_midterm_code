from Node import Node
from cmath import inf, infj

def DFS(G: list[Node], source: Node): 
    """Iterative Version of the Depth First Search Algorithm"""
    for n in G:
        #Initialize all distances to inf
        n.distance = inf
    S: list[Node] = [] #Stack of Nodes
    source.distance = 0 #source node's distance is 0
    explored = [] #list of all explored
    S.append(source)
    while len(S) > 0:
        v = S.pop()
        if v not in explored:
            explored.append(v)
            connections: list[tuple] = v.get_connections()
            for n, w in connections:
                if n not in explored:
                    S.append(n)
                    #relaxation
                    if n.distance > v.distance + w:
                        n.distance = v.distance + w
