#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3


#for this problem, the groups of people who are able to converse can be represented as SCCs
#by finding the largest SCC, we know the largest amount of people who can be kept in the cantina
#without causing any issues.

#logic to set up adjancy list
n = int(input())
nodes = {}
for _ in range(n):
    line = input().split(" ")
    nodes[line[0]] = line[1:]
adjacency_list = {}
for key in nodes:
    adjacency_list[key] = []
    for key2 in nodes:
        if key != key2:
            if (nodes[key][0] in nodes[key2]):
                adjacency_list[key].append(key2)

#now, find the largest SCC with tarjans algo. 
def strongconnect(vertex):
    
    #mark the current vertex as visited while updating its index and lowlink
    global index
    indices[vertex] = index
    lowlink[vertex] = index
    stack.append(vertex)
    on_stack[vertex] = True
    index += 1
    
    # make recusrive calls across all unvisisted neighbouring vertices
    for neighbour in adjacency_list[vertex]:
        if indices[neighbour] == -1:
            strongconnect(neighbour)
            lowlink[vertex] = min(lowlink[vertex], lowlink[neighbour])
        elif on_stack[neighbour]:
            lowlink[vertex] = min(lowlink[vertex], indices[neighbour])
            
    # now, we can get the size of the scc by popping from the stack
    if lowlink[vertex] == indices[vertex]:
        size = 0
        while True:
            popped_v = stack.pop()
            on_stack[popped_v] = False
            size += 1
            if popped_v == vertex:
                global largest_scc
                # update the largest scc
                largest_scc = max(largest_scc, size)
                break
    
#initiate neccessary fields for tarjans
on_stack = {key: False for key in adjacency_list}
indices = {key: -1 for key in adjacency_list}
lowlink = {key: -1 for key in adjacency_list}
stack = []
index = 0
largest_scc = 0

#calling logic for the DFS based strongconnect function
for v in adjacency_list:
    if indices[v] == -1:
        strongconnect(v)
        
# we can now subtract the size of the largest_scc from the total number of people in the 
# cantina to get the # of people who must be kicked out
print(n - largest_scc)
        

    