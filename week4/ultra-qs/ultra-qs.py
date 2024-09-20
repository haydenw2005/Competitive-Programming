#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n = int(input())
array = [int (input()) for _ in range(n)]
inversions = 0

# we need to count the total inversions. the brute force n^2 solutions is super
# easy but sadly its too slow. So instead lets break it up using divide in conquer.
# merge sort will be out vessel for this, as we can count inversions in linear time
# in the merge step. 

#custom implementation of merge sort, sloppy
def mergeCount (arr):
    
    #globalize for simplicity
    global inversions
    n = len(arr)
    
    #base cases. if pair is out of order than we can count 1 inversion
    if (n == 2):
        if arr[0] > arr[1]: 
            inversions += 1
            return [arr[1], arr[0]]
        return arr
    elif (n == 1): return arr
    
    #recusrive subcalls
    mid = (n + 1) // 2
    left_arr = mergeCount(arr[:mid])
    right_arr = mergeCount(arr[mid:])
    
    i = 0
    j = 0
    new_arr = []
    
    #merge step
    while (i < len(left_arr) and j < len(right_arr)):
        if (left_arr[i] > right_arr[j]):
            new_arr.append(right_arr[j])
            j += 1
            
            # here is the key, adding the difference between current position in left_arr
            # and the length of the left_arr, whenever j needs to be incremented (an indiciator
            # of an element being out of order)
            inversions += (len(left_arr) - i)
        else:
            new_arr.append(left_arr[i])
            i += 1
    
    # add whatever sub-array is remaing to new_arr          
    if (i < len(left_arr)):
        new_arr += left_arr[i:]   
    elif (j < len(right_arr)):
        new_arr += right_arr[j:]
            
    return new_arr
            
mergeCount(array)
print(inversions)
