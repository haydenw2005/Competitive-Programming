#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

from collections import deque

# get input
rows, cols = map(int, input().split())
E_line = input().strip().split()
grid = [[int(x) for x in input().split()] for _ in range(rows)]
dist = [[float('inf')] * cols for _ in range(rows)]

# set up bottom row + initial negative edges
neg_edges = set()
for i in range(cols):
    d = grid[rows - 1][i]
    dist[rows - 1][i] = d
    if d < 0:
        neg_edges.add((rows - 1, i))
        
# all possible directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# calculate all negative edges, add to a set. later on we can use these to mark the end of the climb
# (negative edge creates an arbitrage, giving him unlimited energy)
for row in range(rows):
    for col in range(cols):
        if grid[row][col] > 0: continue
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[row][col] + grid[new_row][new_col] < 0:
                        neg_edges.add((row, col))
                        break
                    
#init a queue, which we can for BFS traversal. Add first row before starting.
queue = deque()                        
for i in range(cols):
    if (rows - 1, i) not in neg_edges:
        queue.append((rows - 1, i))

#BFS
while queue:
    row, col = queue.popleft()
    #branch off to neighbours
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            #we hit one of the negative edges. make note of the current energy consumption in dist which
            #we can access later. Don't add any neighbours to the queue so we can cut off this branch of BFS
            if (new_row, new_col) in neg_edges:
                dist[new_row][new_col] = min(dist[row][col], dist[new_row][new_col])
                continue
            #calculate new cost and update distance if we found a shorter path
            cost = grid[new_row][new_col]
            if dist[new_row][new_col] > dist[row][col] + cost:
                dist[new_row][new_col] = dist[row][col] + cost
                queue.append((new_row, new_col))
                
# calcualte the lowest distance 
lowest_dist = float('inf')
for d in dist[0]:
    lowest_dist = min(lowest_dist, d)
    
for row, col in neg_edges:
    lowest_dist = min(lowest_dist, dist[row][col])

if (lowest_dist < 0 or lowest_dist == float('inf')): print(0)
else: print(lowest_dist)
