#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

total_cases = int(input())

def dfs(vertex):
    visited[vertex] = True
    for adjacentVertex in adjacency_list[vertex]:
        if not visited[adjacentVertex]:
            dfs(adjacentVertex)

for _ in range(total_cases):
    n_dom, lines = map(int, input().split())
    adjacency_list = {i: [] for i in range(1, n_dom + 1)}
    in_degree = {i: 0 for i in range(1, n_dom + 1)}
    
    for i in range(lines):
        vertex, neighbour = map(int, input().split())
        adjacency_list[vertex].append(neighbour)
        in_degree[neighbour] += 1 

    unlinked_vertices = [v for v in range(1, n_dom + 1) if in_degree[v] == 0]

    visited = {key: False for key in adjacency_list}
    
    total = 0
    for vertex in unlinked_vertices:
        if not visited[vertex]:
            total += 1
            dfs(vertex)
    
    for vertex in adjacency_list:
        if not visited[vertex]:
            total += 1
            dfs(vertex)
    print(total)