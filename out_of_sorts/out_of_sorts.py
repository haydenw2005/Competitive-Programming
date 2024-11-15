#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n, m, a, c, x_0 = [int(x) for x in input().split()]

# generate the sequence using the provded formula
seq = [x_0]
for i in range(1, n + 1):
    seq.append((a * seq[i - 1] + c) % m)
seq = seq[1:]  

  
total_found = 0

#just run the typical binary search on each element in the sequence. if there is a hit, then increment total_found
for item in seq:
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low + high)//2
        if (seq[mid] == item): 
            total_found += 1
            break
        
        if (seq[mid] > item):
            high = mid - 1
        else:
            low = mid + 1
 
print(total_found)           

    
    