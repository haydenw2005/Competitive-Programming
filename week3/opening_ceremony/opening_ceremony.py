#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n = int(input())
towers = [int(item) for item in input().split()]

#create a dict that stores each unique tower height and how many times 
#it appears as input
tower_counts = {}
for tower in towers:
    if tower in tower_counts:
        tower_counts[tower] += 1
    else:
        tower_counts[tower] = 1

# sort that dict (ik) so we can easily iterate over later
sorted_towers = dict(sorted(tower_counts.items()))

charges = 0

#iterate over each tower height and its count in ascending order
for tower, count in sorted_towers.items():
    tower_height = tower - charges
    
    #if the current height of the tower is greater than the times it appears,
    #then lets remove the towers individuals
    if (tower_height > count):
        charges += count
    else:
        #else, blow up a charge for the total height
        charges += tower_height

print(charges)