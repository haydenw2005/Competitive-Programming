#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

#Run binary search
# Filter out all greater than mid point
    # if filtered row are valid, then we can try with higher midpoitn
    # if filtered row are not valid, then we can try with lower midpoitn
    
#but what about uniques? can we just get the largest unique value then do max bst, unique

n = int(input())

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))


low = 0
high = 10**9 + 1

# the can function. here, we filter out all weights greater than mid. if each row is correct in that each pair is next to each other,
# then we know that we the can is valid. Else, we need to check if there is a higher weight that also breaks correctness.
def can(mid, rows):
    for row in rows:
        filtered_row = list(filter(lambda x: x > mid, row))
        i = 0
        while i < len(filtered_row) - 1: 
            if filtered_row[i] != filtered_row[i + 1]:
                return False
            i += 2

    return True


uniques = set()

# -1 so that max() on empty set does not cause an error
uniques.add(-1)

# loop through one row to see which weights are unique. if it occurs once, it is unique, if it occurs twice, it is not unique
# and is removed after being added the first time. We can assume that all weights that do not exist in this row either exist 
# as a pair in the other row, or do not exist at all. 

for weight in row1:
    if weight not in uniques:
        uniques.add(weight)
    else:
        uniques.remove(weight)

# now we can filter out the uniques from each row. this is a simple way to handle uniques, becuase we can later
# check to see if the max unique weight is greater than that greatest weight of the pairs that need to be moved.
# removing them now ensures correctness and makes the can function much simpler because we only need to worry about pairs.
row1 = list(filter(lambda x: x not in uniques, row1))
row2 = list(filter(lambda x: x not in uniques, row2))

max_uniques = max(uniques)


# perform simple binary search, calling on our can function to check validity
while low < high:
    mid = (low + high) // 2
    if can(mid, [row1, row2]):
        high = mid
    else:
        low = mid + 1
        
print(max(low, max_uniques))
