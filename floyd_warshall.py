# Number of vertices
nV = 6
INF = 999

# Algorithm 
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        sol(dist)

# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")
    print(" ---------------- ")

G = [[0, INF, INF, INF, -1, INF],
         [1, 0, INF, 2, INF, INF],
         [INF, 2, 0, INF, INF, -8],
         [-4, INF, INF, 0, 3, INF],
         [INF, 7, INF, INF, 0, INF],
         [INF, 5, 10, INF, INF, 0]]
floyd(G)