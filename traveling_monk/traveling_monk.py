#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

a, d = [int(i) for i in input().split()]

ascent = []
descent = []
height = 0
for i in range(a):
    h, t = [int(i) for i in input().split()]
    ascent.append((h, t))
    height += h

for i in range(d):
    h, t = [int(i) for i in input().split()]
    descent.append((h, t))

a_pos = 0
d_pos = height

a_time = 0
d_time = 0

a_index = 0
d_index = 0

def calculate_meeting_time(a_pos, d_pos, a_segment, d_segment, a_time, d_time):
    remaining_distance = d_pos - a_pos
    a_time_rem = (a_segment[1] - max(a_time - d_time, 0))
    d_time_rem = (d_segment[1] - max(d_time - a_time, 0))
    if (a_time_rem <= 0 or d_time_rem <= 0):
        print(max(a_time, d_time))
        return
    ascent_speed = a_segment[0] / a_time_rem
    descent_speed = d_segment[0] / d_time_rem
    if (remaining_distance == 0 or (ascent_speed + descent_speed) == 0):
        print(max(a_time, d_time))
        return
    meeting_time = remaining_distance / (ascent_speed + descent_speed)
    print(meeting_time + min(a_time, d_time))

def move_monk(pos, segment, time, index):
    pos += segment[0]
    time += segment[1]
    index += 1
    return pos, time, index

def check_meeting(a_pos, d_pos, a_index, d_index, a_time, d_time):
    if a_pos == d_pos:
        calculate_meeting_time(a_pos, d_pos, ascent[a_index], descent[d_index], a_time, d_time)
        return True
    return False

while True:

    if (a_time < d_time):
        if (a_pos + ascent[a_index][0] <= d_pos):
            a_pos, a_time, a_index = move_monk(a_pos, ascent[a_index], a_time, a_index)
            if check_meeting(a_pos, d_pos, a_index, d_index, a_time, d_time):
                break
       
        else:
            calculate_meeting_time(a_pos, d_pos, ascent[a_index], descent[d_index], a_time, d_time)
            break
    
    elif (d_time < a_time):
        
        if (a_pos <= d_pos - descent[d_index][0]):
            d_pos, d_time, d_index = move_monk(d_pos, (-descent[d_index][0], descent[d_index][1]), d_time, d_index)
            if check_meeting(a_pos, d_pos, a_index, d_index, a_time, d_time):
                break
        
        else:
            calculate_meeting_time(a_pos, d_pos, ascent[a_index], descent[d_index], a_time, d_time)
            break
    else:
        if (a_pos + ascent[a_index][0] < d_pos - descent[d_index][0]):
            a_pos, a_time, a_index = move_monk(a_pos, ascent[a_index], a_time, a_index)
            d_pos, d_time, d_index = move_monk(d_pos, (-descent[d_index][0], descent[d_index][1]), d_time, d_index)
        
        elif (a_pos < d_pos - descent[d_index][0]):
            d_pos, d_time, d_index = move_monk(d_pos, (-descent[d_index][0], descent[d_index][1]), d_time, d_index)
        
        elif (a_pos + ascent[a_index][0] < d_pos):
            a_pos, a_time, a_index = move_monk(a_pos, ascent[a_index], a_time, a_index)
        
        else: 
            calculate_meeting_time(a_pos, d_pos, ascent[a_index], descent[d_index], a_time, d_time)
            break

# # Author: Hayden White
# # It is ok to share my code anonymously for educational purposes
# # ! /usr/bin/python3

# a, d = map(int, input().split())

# ascent = []
# descent = []
# total_height = 0

# # Reading ascent data
# for _ in range(a):
#     h, t = map(int, input().split())
#     ascent.append((h, t))
#     total_height += h

# # Reading descent data
# for _ in range(d):
#     h, t = map(int, input().split())
#     descent.append((h, t))

# # Compute cumulative times and positions for ascent
# a_times = [0]
# a_positions = [0]
# for h, t in ascent:
#     a_times.append(a_times[-1] + t)
#     a_positions.append(a_positions[-1] + h)

# # Compute cumulative times and positions for descent
# d_times = [0]
# d_positions = [total_height]
# for h, t in descent:
#     d_times.append(d_times[-1] + t)
#     d_positions.append(d_positions[-1] - h)

# # Initialize indices for ascent and descent segments
# a_index = 0
# d_index = 0

# while a_index < len(a_times) - 1 and d_index < len(d_times) - 1:
#     # Find the overlapping time interval between the current segments
#     start_time = max(a_times[a_index], d_times[d_index])
#     end_time = min(a_times[a_index + 1], d_times[d_index + 1])

#     if start_time >= end_time:
#         # No overlap; move to the next segment
#         if a_times[a_index + 1] < d_times[d_index + 1]:
#             a_index += 1
#         else:
#             d_index += 1
#         continue

#     # Calculate positions at the start and end of the overlapping interval
#     # For the ascending monk
#     if a_times[a_index + 1] != a_times[a_index]:
#         a_speed = (a_positions[a_index + 1] - a_positions[a_index]) / (a_times[a_index + 1] - a_times[a_index])
#         a_start_pos = a_positions[a_index] + (start_time - a_times[a_index]) * a_speed
#         a_end_pos = a_positions[a_index] + (end_time - a_times[a_index]) * a_speed
#     else:
#         # Monk is resting; speed is zero
#         a_speed = 0
#         a_start_pos = a_positions[a_index]
#         a_end_pos = a_positions[a_index]

#     # For the descending monk
#     if d_times[d_index + 1] != d_times[d_index]:
#         d_speed = (d_positions[d_index + 1] - d_positions[d_index]) / (d_times[d_index + 1] - d_times[d_index])
#         d_start_pos = d_positions[d_index] + (start_time - d_times[d_index]) * d_speed
#         d_end_pos = d_positions[d_index] + (end_time - d_times[d_index]) * d_speed
#     else:
#         # Monk is resting; speed is zero
#         d_speed = 0
#         d_start_pos = d_positions[d_index]
#         d_end_pos = d_positions[d_index]

#     # Check if the monks cross each other in this interval
#     if (a_start_pos - d_start_pos) * (a_end_pos - d_end_pos) <= 0:
#         # They meet in this interval
#         # If the speeds are the same, they meet at the start time
#         if a_speed == d_speed:
#             meeting_time = start_time
#         else:
#             # Calculate the exact meeting time within the interval
#             meeting_time = (d_start_pos - a_start_pos) / (a_speed - d_speed) + start_time
#         # Output the meeting time with 6 decimal places
#         print(f"{meeting_time:.6f}")
#         break

#     # Move to the next segment
#     if a_times[a_index + 1] < d_times[d_index + 1]:
#         a_index += 1
#     else:
#         d_index += 1
