#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# Chat link: NONE

# Can use simple UnionFind data structure, which was just taught in 251
# Implmentation adapted from slides
class UnionFind: 
    def __init__(self):
        self.parent = {}
        self.size = {}    
        
    # add a person to the network if they are not already in it
    def add_person(self, name):
        if name not in self.parent:
            self.parent[name] = name
            self.size[name] = 1
    
    # find the root of the person, while compressing the path
    def find(self, name):
        if self.parent[name] != name:
            self.parent[name] = self.find(self.parent[name])
        return self.parent[name]
    
    # union the two people into the same network
    def union(self, name1, name2):
        # add the two people to the network if they are not already in it
        self.add_person(name1)
        self.add_person(name2)
        
        # find the roots of the two people
        root1 = self.find(name1)
        root2 = self.find(name2)
        
        # if not already in the same network, union them
        if root1 != root2:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        
        # return the size of the network of the first person
        return self.size[self.find(name1)] 

#process each case
num_cases = int(input())
for _ in range(num_cases):
    num_friends = int(input())
    uf = UnionFind()
    # go line by line, and union the two friends
    for __ in range(num_friends):
        friend1, friend2 = input().split()
        network_size = uf.union(friend1, friend2)
        print(network_size)    
    

