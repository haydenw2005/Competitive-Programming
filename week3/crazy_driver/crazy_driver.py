#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# TODO add input selection

total_gates = int(input())
fees = list(map(int, input().split()))
open_times = list(map(int, input().split()))

cost = 0
hours = 1
current_road = 0

gate_values = [0] * (total_gates - 1)
minimum_index = 0

open_times = open_times[1:]

for index, gate in enumerate((open_times)):
    gate_values[index] += 1
    
    # we want to track the current minimum index, this is where we want to 
    # the driver to "wait" as it will accumalte the least code
    if (fees[minimum_index] > fees[index]):
        minimum_index = index

    # total time needed to wait before passing next gate
    hours_to_pass = gate - hours
     
    # if needs to wait, add those hours to the minimum to minimize costs   
    if (hours_to_pass > 0):
    
        # to accomdate for the driver driving "backwards"
        if (hours_to_pass % 2 == 1):
            hours_to_pass += 1
            
        # get the total hours that the driver needs to wait before driving
        # past the gate
        gate_values[minimum_index] += hours_to_pass   
        hours += hours_to_pass
    
    hours += 1
    
    
# final calcualtion step, multiply the total time waited at teach road
# by the cost of each road
final_val = 0
for index, value in enumerate(gate_values):
    final_val += value * fees[index]
    
print(final_val)
    

    
    




# unlocked_gate = 1
# best_road = 0

# is_moving_forward = True

# while unlocked_gate < total_gates:
    
#     hours += 1
        
#     future_hours = hours
#     while (unlocked_gate < total_gates and open_times[unlocked_gate] <= future_hours):
#         unlocked_gate += 1
#         future_hours += 1
#         if (unlocked_gate < len(fees) + 1 and fees[unlocked_gate - 1] <= fees[best_road]):
#             best_road = unlocked_gate - 1
    
#     if (unlocked_gate == total_gates): break
    

#     cost += fees[current_road]
    
#     if (is_moving_forward and current_road < best_road):
#         current_road += 1
#     else:
#         is_moving_forward = not is_moving_forward
            
        
             
#     # print("road: ",current_road, "unlocked_gate: ", unlocked_gate, "best:", best_road, "cost:", cost, "ISMOVINGFORWARD:", is_moving_forward, hours)
    
# # print("end!", current_road, len(fees), "ISMOVINGFORWARD:", is_moving_forward)
# if (not is_moving_forward): current_road += 1
# while (current_road < len(fees)):
#     cost += fees[current_road]
#     current_road += 1
    
# print(cost)