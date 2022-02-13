from Node import Node
from cmath import inf, infj

def visit(n: Node, visited: list[Node], S: list[Node]):
    visited.append(n)
    for c, w in n.get_connections():
        if c not in visited:
            visit(c, visited, S)

    S.append(n)

def topological_sort(G: list[Node]) -> list[Node]:
    l = []
    S = []
    visited = [] #visited Nodes
    for n in G:
        if n not in visited:
            visit(n, visited, S)

    while len(S) > 0:
        out = S.pop()
        l.append(out)
    return l

def main():
    n1 = Node(0)
    n2 = Node(1)
    n3 = Node(2)
    n1.add_node(n2, 1)
    n1.add_node(n3, 1)
    G = [n1, n2, n3]
    l = topological_sort(G)
    for n in l:
        print(n.id)
    
if __name__ == "__main__":
    main()
