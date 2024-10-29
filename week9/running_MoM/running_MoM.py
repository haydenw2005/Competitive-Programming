#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# this question is essentially asking which locations are in a cycle, which represnet a sequence
# of locations that can be cycled forever

#set up adjacency list
n = int(input())
adjacency_list = {}
visited = {}
for _ in range(n):
    line = input().split(" ")
    if line[0] not in adjacency_list:
        adjacency_list[line[0]] = []
    if line[1] not in adjacency_list:
        adjacency_list[line[1]] = []
    if line[0] not in visited:
        visited[line[0]] = False
    if line[1] not in visited:
        visited[line[1]] = False
    adjacency_list[line[0]].append(line[1])

# DFS function that returns True if a cycle exists    
def dfs(vertex, visited):
    visited[vertex] = True
    for adjacentVertex in adjacency_list[vertex]:
        # if we try to visit a vertex we have already visited, then it must be a cycle
        if not visited[adjacentVertex]:
            if dfs(adjacentVertex, visited):
                return True
        else:
            return True
    # set visited[vertex] to reset state across other recusrve branches
    visited[vertex] = False
      
    return False  

try:
    while True:
        # calling logic, reading in the list of cities from input that we want to check
        vertex_to_check = (input())
        # if DFS returns True, then we know a location is safe
        if dfs(vertex_to_check, visited):
            print(vertex_to_check, "safe")
        else:
            print(vertex_to_check, "trapped")
except EOFError:
    pass
