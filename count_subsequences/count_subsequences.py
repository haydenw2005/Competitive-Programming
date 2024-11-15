# Author: Hayden White
# It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n = int(input())
target = 47

# loop through each test case
for _ in range(n):
    input()  
    seq_len = int(input())
    num_seq = list(map(int, input().split()))

    # hash map to store prefix sum frequencies
    prefix_count_cache = {0: 1}  
    current_sum = 0
    count = 0

    # iterate through each number in the sequence
    for num in num_seq:
        current_sum += num
        
        # check if there exists a prefix such that is equal to current_sum - target
        # if it exists, we know that a valid subsequence has been found, and now we can add the frequency of that prefix sum to 
        # the total count
        if current_sum - target in prefix_count_cache:
            count += prefix_count_cache[current_sum - target]

        # increment the prefix sum frequency in the hash map
        if current_sum in prefix_count_cache:
            prefix_count_cache[current_sum] += 1
        else:
            prefix_count_cache[current_sum] = 1

    print(count)
