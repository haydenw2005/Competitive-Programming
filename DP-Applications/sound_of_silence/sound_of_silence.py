# Author: Hayden White
# It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

from collections import deque

n, m, c = [int(x) for x in input().split()]
seq = list(map(int, input().split()))

i = 0
j = 0

hit_indices = []

# can use deque to store the current min/max of the sliding window
# will store min/max at first element of each queue
min_deque = deque()
max_deque = deque()

while j < n:
    
    # if last element greater than the new element at j, pop from deque
    while min_deque and seq[min_deque[-1]] > seq[j]:
        min_deque.pop()
    # add new index to min_deque
    min_deque.append(j)

    # same operation as above but for max_deque
    while max_deque and seq[max_deque[-1]] < seq[j]:
        max_deque.pop()
    max_deque.append(j)


    # remove all elements that are no longer in bounds of the current window
    if min_deque and min_deque[0] < i:
        min_deque.popleft()
    if max_deque and max_deque[0] < i:
        max_deque.popleft()

    # if window size is m, check if the difference between max and min is less than c
    # also, the conditional ensures the window will never be greater than m
    if j - i + 1 == m:
        val = seq[max_deque[0]] - seq[min_deque[0]]
        if val <= c:
            hit_indices.append(i + 1)
            
        # increment i to slide the window
        i += 1
    
    # increment j to expand the window
    j += 1

# sort and print the result, or NONE if empty
if hit_indices:
    hit_indices.sort()
    for index in hit_indices:
        print(index)
else:
    print("NONE")
