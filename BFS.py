from cmath import inf
from Node import Node

def BFS(G: list[Node], source: Node):
    #Set distances to infinity
    for n in G:
        n.distance = inf
    Q: list[Node] = [] #Queue of nodes
    source.distance = 0 #Source distance is zero
    explored = [] #explored nodes
    Q.append(source)
    while len(Q) > 0:
        v = Q.pop(0) # Gets the first element of the Queue
        explored.append(v) #explored v
        connections: list[tuple] = v.get_connections() #Gets the connections of v
        for n, w in connections:
            #edge relaxation
            if n not in explored:
                Q.append(n)# add child to Queue if not explored already
                if n.distance > v.distance + w: #relaxation
                    n.distance = v.distance + w;

