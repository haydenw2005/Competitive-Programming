#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n, m = [int(x) for x in input().split()]

#sort for binary search
can_sizes = [int(input()) for _ in range(n)]
can_sizes.sort()

paint_needed = [int(input()) for _ in range(m)]

total_waste = 0

#perform binary search on paint amount joe needs, finding the closest that he requires.
for amount in paint_needed:
    left = 0
    right = n - 1
    while (left <= right):
            
        mid = (left + right) // 2
        
        if (amount > can_sizes[mid]):
            left = mid + 1
        else:
            right = mid - 1
    
    # can size must always be grater than the amount needed. So if we end up smaller index, increment by one.
    if (can_sizes[mid] < amount): mid += 1
    
    total_waste += can_sizes[mid] - amount

            

print(total_waste)