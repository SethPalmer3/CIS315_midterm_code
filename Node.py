from cmath import inf


class Node:
    def __init__(self):
        #ID of the node
        self.id: int = None
        #All the nodes that this Node points to
        self.children: list["Node"] = []
        #stores the weights to the children indexes must be the same
        self.weight: list[float] = []
        self.distance = inf
    
    def get_connections(self) -> list["Node"]:
        """Returns all the connections in a list of tuples (Node, weight)"""
        l = []
        for i in range(len(self.children)):
            l.append(tuple(self.children[i], self.weight[i]))
        return l

    def add_node(self, n: "Node", w: float) -> None:
        """Adds a connection between self and n with a weight of w"""
        self.children.append(n)
        self.weight.append(w)