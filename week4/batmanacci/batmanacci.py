#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n, k = [int(x) for x in input().split()]

# Here, we precompute the length of batmanacci strings
# The first srings, N and A, are both of length 1. Now we compute from there.
length_sequence = [0] * (n + 2)
length_sequence[1] = length_sequence[2] = 1
for i in range(3, n + 1):
    length_sequence[i] = length_sequence[i - 2] + length_sequence[i - 1]


#now perform a sort of binary search
while True:
    
    # base cases, the problem is solved
    if n == 1:
        print('N')
        break
    elif n == 2:
        print('A')
        break
    
    #if k greater than length_sequence[n-2], then k must be in range of length_sequence[n-1]
    #therfore, lets reduce k by length_sequence[n-2] and decrement n to look inside length_sequence[n-1]
    elif k > length_sequence[n-2]:
        k -= length_sequence[n-2]
        n -= 1
    
    #here we know k must be in range of length_sequence[n-2], so lets look inside length_sequence[n-2]
    else:
        n -= 2
