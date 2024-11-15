#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

#CHAT LINK: https://chatgpt.com/share/67295ab3-e2a0-800a-814b-dbf4b9514812

# Can use simple UnionFind data structure, which was just taught in 251
# Implmentation adapted from slides
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0  
        
    # add a person to the network if they are not already in it
    def add_person(self, id1):
        if id1 not in self.parent:
            self.parent[id1] = id1
            self.count += 1
    
    # find the root of the person, while compressing the path
    def find(self, id1):
        if self.parent[id1] != id1:
            self.parent[id1] = self.find(self.parent[id1])
        return self.parent[id1]
    
    # union the two people
    def union(self, id1, id2):
        self.add_person(id1)
        self.add_person(id2)
        
        root1 = self.find(id1)
        root2 = self.find(id2)
        
        if root1 != root2:
            self.parent[root2] = root1  
            self.count -= 1
    
    # check if two people are connected
    def connected(self, id1, id2):
        if id1 not in self.parent or id2 not in self.parent:
            return False
        return self.find(id1) == self.find(id2)

num_ppl = int(input())

# start by initializing the UnionFind data structure with people
union_find = UnionFind()
for i in range(num_ppl):
    person_id = i + 1
    union_find.add_person(person_id)

# map a given number to the list of people it connects
number_to_people = {}
for i in range(num_ppl):
    line = [int(x) for x in input().split()]
    person_id = i + 1
    for num in line[1:]:
        if num not in number_to_people:
            number_to_people[num] = []
        number_to_people[num].append(person_id)

output = []
# loop through each connection list, and try to build the minimum spanning tree.
for num, people in number_to_people.items():
    for i in range(1, len(people)):
        if not union_find.connected(people[0], people[i]):
            output.append((people[0], people[i], num))
            union_find.union(people[0], people[i])
            
# if union_find count is 1, then we know that
# everyone is connected, so we proceed with adding the edges to the output
if union_find.count == 1:
    for line in output:
        print(*line)
else:
    print("impossible")