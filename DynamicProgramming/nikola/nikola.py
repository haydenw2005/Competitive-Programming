#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

n = int(input())
costs = [int(input()) for i in range(n)]

cache = {}

# our recursive function to calculate the minimum cost of jumping to the end of the array
def calc_jump(prev, pos):
    # if we are out of bounds, return infinity, so that the min function chooses the other option
    if pos < 1 or pos > n: 
        return float('inf')
    
    # if we are at the final spot, return the cost of the last position
    elif pos == n: 
        return costs[n - 1]
    
    # if the result is cached, return the cached result
    elif (prev, pos) in cache:
        return cache[(prev, pos)]
    
    # calculate the cost of jumping forward and backward
    forward_jump = calc_jump(prev + 1, pos + prev + 1)
    backwards_jump = calc_jump(prev, pos - prev)
    
    #choose the best move, which is the least costly
    best_move = min(forward_jump, backwards_jump)
    
    # add the cost of the current position to the best move, then cache the result for future use
    cache[(prev, pos)] = costs[pos - 1] + best_move
    
    # return the total cost up to this point
    return cache[(prev, pos)]

# start the recursive function with the first jump from 1 to 2
result = calc_jump(1, 2)

# print the result
print(result)

