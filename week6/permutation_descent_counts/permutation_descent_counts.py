#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# the max number of elements in the permutation
MAX_N = 101

# initialize the table. 
table = [[0] * MAX_N for _ in range(MAX_N)]

# set the base case. 
for i in range(1, MAX_N):
    table[i][i - 1] = 1

# fill in the table. remember, we dont care about cases where there are more descents 
# than elements in the permutation, which is why we start i at j + 2.

for j in range(0, MAX_N): # the number of descents in the permutation
    for i in range(j + 2, MAX_N): # the number of elements in the permutation
        
        #(j + 1) * table[i - 1][j] all the new ways to "replace" a descent
        #(i - j) * table[i - 1][j - 1] all the new ways to "add" a descent
        table[i][j] = (j + 1) * table[i - 1][j] + (i - j) * table[i - 1][j - 1]


total = int(input())

# map the input to the table and print the result
for i in range(total):
    k, n, v = map(int, input().split())
    descents = table[n][v]
    
    #print the remainder, results can be very large
    print(k, descents % 1001113)