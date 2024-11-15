#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# Chat Link: NO GEN AI USED FOR THIS PROBLEM. 

import heapq

n = int(input())

# init requisite datastuctures
start_cost = []
adj_list = [[] for _ in range(n)]
rev_adj_list = [[] for _ in range(n)]
in_degree = [0] * n

# process each meeting to build the graph and store start times
for i in range(n):
    line = [int(x) for x in input().split()]
    start_cost.append(line[0])
    for item in line[2:2 + line[1]]:
        adj_list[item - 1].append(i)      # Build forward dependency graph for topological sort
        rev_adj_list[i].append(item - 1)  # Build reverse dependency graph for DFS
        in_degree[i] += 1


visited = [False] * n
max_dp = [0] * n

# iterative DFS function to update the maximum durations (max_dp). Every "parent" meeting should have the same maximum cost as
# its greatest cost child meeting to ensure that topics with high impact depedencies are sceduled earlier, minimizing the accumlated
# recap time for these topics and reducing the length of the longest meeting overall..
def dfs(start_vertex, cost):
    stack = [(start_vertex, cost)]
    while stack:
        vertex, curr_cost = stack.pop()
        if visited[vertex]: #skip if already visited
            continue
            
        visited[vertex] = True
        max_dp[vertex] = curr_cost
        
        for neighbour in rev_adj_list[vertex]:
            stack.append((neighbour, curr_cost))

# sort indices by start_cost in descending order and process in that order. by doing this descending order of initial costs, we save 
# a lot of time by leveaging a pruning technique. Starting from the highest base costs, we ensure that each DFS explores topics in 
# order of their maximum impact. This way, when we reach topics with lower base costs, they've likely already been updated by earlier DFS runs....
# Thus, we can skip DFS calls for topics where the updated max_dp value already exceeds the base cost (pruning),
# avoiding unnecessary calculations and redundant DFS calls. Without this logic, the code would be many magnitudes slower
for i in sorted(range(n), key=lambda x: start_cost[x], reverse=True):
    # Only initiate DFS if the current topic's max_dp is less than its base cost.
    # This ensures that we only perform DFS when there's a potential to increase the max_dp value, which is key to the above blurb
    if max_dp[i] < start_cost[i]:
        dfs(i, start_cost[i])


# now we can move onto to the typical topological sort logic

#use a heap so that we are always using the largest items first, to try our best to 
#counter balance the growing expense of having back to back meetings, which increase length by 1.
no_deps = [(-max_dp[i], i) for i in range(n) if in_degree[i] == 0]
heapq.heapify(no_deps)

# used: kahns algo: https://en.wikipedia.org/wiki/Topological_sorting
sorted_agenda = []
meeting_count = 0          
max_meeting = 0

# run kahns algo on the directed acyclic graph to get the optimal order  
while len(no_deps) != 0:
    _, vertex = heapq.heappop(no_deps)
    sorted_agenda.append(vertex)
    # keep track of the current max meeting
    max_meeting = max(max_meeting, start_cost[vertex] + meeting_count)
    for neighbor in adj_list[vertex]:
        in_degree[neighbor] -= 1 # mimicks edge removal typical of Kahn;s algo
        if in_degree[neighbor] == 0:
            heapq.heappush(no_deps, (-max_dp[neighbor], neighbor))

    meeting_count += 1

#print the final result, the longest recorded meeting    
print(max_meeting)