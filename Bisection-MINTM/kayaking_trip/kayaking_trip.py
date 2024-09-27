#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

counts = (b_count, n_count, e_count) = [int(i) for i in input().split()]
vals = (b_val, n_val, e_val) = [int(i) for i in input().split()]


canoes = [int(i) for i in input().split()]
canoes.sort()

m = len(canoes)
low = 0
high = 100000 * 1000 * 2 + 1

# the can function. It checks if it is possible to pair participants in each canoe such that their 
# combined strength is greater than or equal to the threshold (mid).
def can(mid):
    local_counts = list(counts)
    
    for canoe in canoes:
        valid = False
        
        # loop through each competence level
        for i in range(3):
            if local_counts[i] > 0:
                
                # decrement to simluate without replacement, will incremenet later if valid and need
                # to run again against other canoe weights
                
                local_counts[i] -= 1
                
                # loop through all other competence levels
                for j in range(i, 3):
                    if local_counts[j] > 0:
                        local_counts[j] -= 1
                        
                        #if a single two person combination is valid, break and move to next canoe
                        # [(vals[i] + vals[j]) * canoe] will always be the lowest valid combo, as the vals tuple is sorted by competence.
                        if (vals[i] + vals[j]) * canoe >= mid:
                            valid = True
                            break
                        local_counts[j] += 1
                        
                if valid:
                    break
                local_counts[i] += 1
                      
        # if no valid combination is found for a single canoe, return False
        if not valid:
            return False
        
    return True

# perform simple binary search, calling on our can function to check validity
while (low < high):
    mid = (low + high) // 2
    if (can(mid)):
        low = mid + 1
    else:
        high = mid 


print(low - 1)
