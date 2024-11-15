#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# get input
total_items = int(input())
item_costs = [int(x) for x in input().split()]
total_orders = int(input())
order_costs = [int(x) for x in input().split()]

# save the max order_cost for later, and then initialize the cache
max_order = max(order_costs)
cache = [None] * (max_order + 1)
cache[0] = -1  

for item_index, item in enumerate(item_costs):
    for i in range(item, max_order + 1):
        
        # if any "child" combination is ambiguous, so is the current combination
        if cache[i - item] == "Ambiguous":
            cache[i] = "Ambiguous"
            continue

        # if the current combination minus the item cost is not none, we can add the index to the combination at i
        # later down the line, we can use these indices to track backwards to determine the full combo
        elif cache[i - item] is not None:
            
            # if unmarked, mark it as the index
            if cache[i] is None:
                cache[i] = item_index  
            
            # if already marked, mark as ambiguous, since we can have multiple combinations that are the same
            elif cache[i] != item_index:
                cache[i] = "Ambiguous"

# now we can just set all remaining values to impossible, since we know that we have "marked" all possible combinations
# either as ambigous or as an index, leaving only the impossible values as None
for i in range(1, max_order + 1):
    if cache[i] is None:
        cache[i] = "Impossible"

# now we can do a neat backtracking step for each order_cost
for order in order_costs:
    
    # if the order is impossible or ambiguous, print the result
    if cache[order] == "Impossible": print("Impossible")
    elif cache[order] == "Ambiguous": print("Ambiguous")
    
    # otherwise, lets calculate the full, unique combination
    else:
        combination = []
        current_cost = order
        
        # now, starting at the order cost, we can work our way back to 0, adding the index to the combination each time
        while current_cost > 0:
            
            # get the cached_index at the current cost
            cached_index = cache[current_cost]
            
            # add the cached_index to the combination
            combination.append(cached_index + 1)  
            
            # subtract the item cost from the current cost. this is the key to working backwards.
            # we use this to get the rest of of the indices
            current_cost -= item_costs[cached_index]
        
        # alas, print the sorted combination
        print(" ".join(map(str, sorted(combination))))