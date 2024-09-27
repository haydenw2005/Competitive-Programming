#Hayden White

#Same code as Christopher Li Gou, my thursday partner

import math

# can function to check if possible
def can(list, partitions, max):
    partition = partitions
    current_counter = 0
    
    # what we are doing here is adding items to a box until we cant add anymore, then continuing with the next box, 
    # until we have used exhausted all the items. Then, we check how many partiions we have left (boxes remaining), and if there are more than 0,
    # we know that this maximum is possible. If it is not possible, we know that the maximum is too low, and we need to
    # increare it in our search. 
    
    for item in list:
        if current_counter + item <= max:
            current_counter += item
        else:
            partition -= 1
            current_counter = item
            
    if partition > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    
    # get inputs and set max and min
    initial = [int(i) for i in input().split()]
    items = initial[0]
    partitions = initial[1]
    item_list = [int(i) for i in input().split()]
    minimum = max(item_list)
    maximum = items * max(item_list)
    
    # bisection search across the solution space. our anwser is the lowest possible maximum that 
    #that satisfies the can function.
    while minimum < maximum:
        average = math.floor((minimum + maximum) / 2)
        answer = can(item_list, partitions, average)
        if answer == 1:
            maximum = average
        else:
            minimum = average + 1

    print(maximum)
