#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys

h, c = input().split(" ")
h = int(h) #number of times ask coworker
c = int(c) # total coworkers

max_annoyance = 0
coworkers = []

#make sure to sort
for i in range(c):
    a, d = input().split(" ")
    coworkers.append([int(a), int(d)])
    

#implement max heap

i = 0
count = 0
while (count <= h):
    #if (i >= len(coworkers) - 1): break
    currentAnnoyance = coworkers[i][0]
    while (currentAnnoyance <= coworkers[i + 1][0] + coworkers[i + 1][1]):
        currentAnnoyance += coworkers[i][1]
        count += 1
        
    print(currentAnnoyance, coworkers[i], coworkers[i + 1][0] + coworkers[i + 1][1])
    max_annoyance = max(max_annoyance, currentAnnoyance)
    
    i += 1 
    

print("max:", max_annoyance)

# use coworkers with low inital costs
# negative_weight = 0
# for coworker in coworkers:
#     if (coworker[0] < lowest_annoyance[0]):
#         h -= 1
    


#another idea
#sort coworkers by annoyance
#start with lowest and utilize them until they are more annoyed than the person in front of them
#move to he next person
