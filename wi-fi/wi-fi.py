# Author: Hayden White

def can_place_access_points(houses, n, max_dist):
    # Initialize the count of access points
    count = 1
    
    last_position = houses[0]

    for i in range(1, len(houses)):
        # If max distance is too big, then we must place a new access point. If we have placed to many access
        # points, then we know this distance is not possible.
        if houses[i] - last_position > max_dist * 2:
            count += 1
            last_position = houses[i]
            if count > n:  # Too many access points needed
                return False
    return True

num_cases = int(input())

for _ in range(num_cases):
    # Initialize input variables
    n, m = [int(x) for x in input().split()]
    houses = sorted([int(input()) for _ in range(m)])  # Sort the house positions

    # Binary search for the minimum possible maximum distance
    low, high = 0, (houses[-1] - houses[0]) / 2
    answer = high
    
    while high - low > 1e-3:  # Search until the difference is small enough
        mid = (low + high) / 2
        
        # use can function to check if we can place access points
        if can_place_access_points(houses, n, mid):
            answer = mid
            high = mid
        else:
            low = mid

    # Output the answer rounded to 1 decimal place
    print(f"{answer:.1f}")
