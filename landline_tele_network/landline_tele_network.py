#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3
import heapq

# Can use simple UnionFind data structure, which was just taught in 251
# Implmentation adapted from slides
class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)} 
        self.size = {i: 1 for i in range(1, n + 1)}

    def find(self, building_id):
        if self.parent[building_id] != building_id:
            self.parent[building_id] = self.find(self.parent[building_id])
        return self.parent[building_id]
    
    def union(self, b1, b2):
        root1 = self.find(b1)
        root2 = self.find(b2)
        
        if root1 != root2:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            return True
        return False

num_buildings, num_connections, num_insecure = map(int, input().split())

# If less connections than buildings, then an MST is impossible
if num_connections < num_buildings - 1:
    print("impossible")
    exit()

insec_bldgs = set(map(int, input().split()))

# Create two min heaps, one for safe edges and one for insecure edges
# With these heaps, we will build an MST that connects all buildings, ensuring that
# an insecure building is only connected to at most one other building
safe_edges = []
unsafe_edges = []

for _ in range(num_connections):
    b1, b2, cost = map(int, input().split())
    if b1 in insec_bldgs or b2 in insec_bldgs:
        unsafe_edges.append((cost, b1, b2))
    else:
        safe_edges.append((cost, b1, b2))
        
heapq.heapify(safe_edges)
heapq.heapify(unsafe_edges)

uf = UnionFind(num_buildings)
total_cost = 0
edges_used = 0

# step 1, connect safe buildings, creating a "safe" MST
while safe_edges and edges_used < num_buildings - 1 - num_insecure:
    cost, b1, b2 = heapq.heappop(safe_edges)
    if uf.union(b1, b2):
        total_cost += cost
        edges_used += 1
        
# step 2, connect insecure buildings, finishing the MST
while unsafe_edges and edges_used < num_buildings - 1:
    cost, b1, b2 = heapq.heappop(unsafe_edges)
    
    # If the building is already connected to another insecure building, skip it
    if b1 in insec_bldgs and uf.size[uf.find(b1)] > 1:
        continue
    if b2 in insec_bldgs and uf.size[uf.find(b2)] > 1:
        continue
    # If both buildings are insecure, then we know we must skip it (unless they are the only two buildings)
    if b1 in insec_bldgs and b2 in insec_bldgs and num_buildings > 2:
        continue
    
    # Otherwise, connect the buildings and add the cost
    if uf.union(b1, b2):
        total_cost += cost
        edges_used += 1

# If we have used enough edges to connect all buildings, print the total cost
if edges_used == num_buildings - 1:
    print(total_cost)
else:
    print("impossible")



