# Author: Hayden White
# It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# Chat link: NONE

# floyd warshall algorithm to find all pairs shortest path. see source below for inspiration
# https://stackoverflow.com/questions/15709277/floyd-warshall-with-negative-cycles-how-do-i-find-all-undefined-paths

def floydWarshall(graph, n):
    # initialize dist as a deep copy of graph
    dist = [row[:] for row in graph]
    
    # typical floyd warshall algorithm
    for k in range(n):
        for i in range(n):
            if dist[i][k] == float('inf'): # prune, if no path to k, skip   
                continue
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # mark all paths in a negative cycle
    for k in range(n):
        if dist[k][k] < 0: 
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = float('-inf')
    
    return dist

# loop thru test cases until reach 0 0 0
while True:
    n, m, q = map(int, input().split())
    if n + m + q == 0:
        break
    
    # initialize n x n graph with 0 on the diagonal and inf everywhere else
    graph = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    
    #initialize graph with edges
    for _ in range(m):
        u, v, w = map(int, input().split())
        if u != v:
            graph[u][v] = min(graph[u][v], w) 
        elif w < 0:
            graph[u][v] = float('-inf') # negative cycle if negative self loop
    
    #generate all pairs shortest path with floyd warshall
    dist = floydWarshall(graph, n)

    #process queries
    for _ in range(q):
        u, v = map(int, input().split())
        if dist[u][v] == float('inf'):
            print("Impossible")
        elif dist[u][v] == float('-inf'):
            print("-Infinity")
        else:
            print(dist[u][v])
    
    print()
