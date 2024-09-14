#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# looked up: "python cache function calls" for memoization
# found: https://stackoverflow.com/questions/815110/is-there-a-decorator-to-simply-cache-function-return-values
from functools import lru_cache

n = int(input())

recital_groups = [set(input().strip()) for _ in range(n)]

#calculate the cost of each group with edvery other group as an adjacency matrix
#will save us time when calculating permutations
recital_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        cost = len(recital_groups[i].intersection(recital_groups[j]))
        row.append(cost)
    recital_matrix.append(row)

# when calculating permutations, we are making many of the same calls.
# caching the results will reduce the time complexity of the program by a lot (see top for source)

# here, we are calculating the cost of every permutation across total # of quick changes
@lru_cache(maxsize=None)
def brute_find_lowest(start, visited_bitmask):
    
    # use a bitmask to efficiently track which groups have been visited
    # each bit in the bitmask represents a group
    # if (1 << n) - 1 is reached, then all groups have been visited
    if visited_bitmask == (1 << n) - 1:
        return 0
    
    lowest = float('inf')
    
    #create a bunch of recusrive sub calls to simulate all possible permutations
    for index in range(n):
        if not (visited_bitmask & (1 << index)):
            new_visited = visited_bitmask | (1 << index)
            val = brute_find_lowest(index, new_visited) + recital_matrix[start][index]
            lowest = min(lowest, val)
    
    return lowest

# now find the lowest cost when starting with every group    
lowest = min(brute_find_lowest(i, 1 << i) for i in range(n))

print(lowest)
