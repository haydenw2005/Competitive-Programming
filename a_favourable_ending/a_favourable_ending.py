#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

num_cases = int(input())

def search_endings(event, possible_endings, visited):
    if event in visited or event not in event_children:
        return 0
    
    visited.add(event)
    children = event_children[event]
    
    if isinstance(children, str):
        visited.remove(event)
        return 1 if children == "favourably" else 0
    
    if event in possible_endings:
        visited.remove(event)
        return possible_endings[event]
    
    total = 0
    for child in children:
        total += search_endings(child, possible_endings, visited)
    
    possible_endings[event] = total
    visited.remove(event)
    return total
    

for _ in range(num_cases):
    num_events = int(input())
    event_children = {}
    for _ in range(num_events):
        event_info = input().split()
        if (len(event_info) == 2):
            event_children[int(event_info[0])] = event_info[1]
        else:
            event_info = list(map(int, event_info))
            event_children[event_info[0]] = event_info[1:]
    
    possible_endings = {}
    result = search_endings(1, possible_endings, set())
    print(result)