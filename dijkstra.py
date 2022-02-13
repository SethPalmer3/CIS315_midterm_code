import imp
from Node import Node
from cmath import inf

def get_smallest_dist(Q: list[Node]):
    best_n = 0
    best_dist = Q[best_n].distance
    for n in range(1, len(Q)):
        if Q[n].distance < best_dist:
            best_n = n
            best_dist = Q[n].distance
    best = Q.pop(best_n)
    return best

def dijkstra(G: list[Node], source: Node) -> list[Node]:
    previous = []
    Q = [] #priority Queue
    for n in G:
        n.distance = inf # initialize all distances to inf
        previous.append(None) #set the previous list to None
        Q.append(n)
    source.distance = 0

    while len(Q) > 0:
        u = get_smallest_dist(Q)
        for c, w in u.get_connections():
            dist = u.distance + w
            if dist < c.distance:
                c.distance = dist
                previous[c.id] = u

def main():
    n1 = Node(0)
    n2 = Node(1)
    n3 = Node(2)
    n1.add_node(n2, 1)
    n1.add_node(n3, 1)
    G = [n1, n2, n3]
    dijkstra(G, n1)
    for n in G:
        print(n.distance)

if __name__ == "__main__":
    main()