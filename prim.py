"""
Prim's Alogrithm for 315 midterm

Madeline Porcaro
"""

INF = 9999999

# number of vertices 
N = 5

#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

print("Edge: Weight\n")

while(no_edge < N - 1): 
    minimum = INF
    x = 0
    y = 0
    for i in range(N):
        if (selected_node[i]):
            for j in range(N):
                # if the node is not selected but exists as an edge
                if ((not selected_node[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        # edge become new minimum
                        minimum = G[i][j]
                        #  x and y become i and j for next iteration
                        x = i
                        y = j
    print(f'{x} - {y} : {G[x][y]}')
    selected_node[y] = True
    no_edge += 1