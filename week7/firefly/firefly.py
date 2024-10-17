#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n, h = map(int, input().split())

low_obstacles = []
high_obstacles = []

#split input in low and high obstacles
for i in range(n):
    height = int(input())
    if i % 2 == 0:
        low_obstacles.append(height)
    else:
        high_obstacles.append(height)
        
        
# now, lets create an array to store the number of collisions from the bottom obstacles 
# for each level
low_obstacles.sort()
low_obstacle_collisions = [0] * h
current_height = 0

for index, item in enumerate(low_obstacles):
    #if next item is greater than current height, update collisions for all levels in between
    if (item > current_height):
        for i in range(current_height, item):
            low_obstacle_collisions[i] = len(low_obstacles) - index
        current_height = item
    
        

# now, lets create an array to store the number of collisions from the top obstacles
# for each level
high_obstacles.sort(reverse=True)
high_obstacle_collisions = [0] * h
current_height = 0

for index, item in enumerate(high_obstacles):
    item_h = (h) - item 
    #if next item is greater than current height, update collisions for all levels in between
    if (item_h > current_height):
        for i in range(current_height, item_h):
            high_obstacle_collisions[i] = index
        current_height = item_h  

# update for remaining levels
for i in range(current_height, h):
    high_obstacle_collisions[i] = len(high_obstacles)
    
# now, lets calculate the total number of collisions for each level
level_collisions = []
for i in range(h):
    level_collisions.append(high_obstacle_collisions[i] + low_obstacle_collisions[i])

# get minimum collisions and count how many times it occurs
min_collisions = min(level_collisions)
min_count = level_collisions.count(min_collisions)

# print result
print(min_collisions, min_count)
