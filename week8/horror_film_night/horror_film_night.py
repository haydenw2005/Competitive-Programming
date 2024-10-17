#Author: Hayden White


first_preferences = sorted([int(i) for i in input().split()][1:])   
second_preferences = sorted([int(i) for i in input().split()][1:])

n = len(first_preferences)
m = len(second_preferences)

# Initialize two pointers for Emma's and Marcos' lists of preferences
i, j = 0, 0
total = 0
last_disliked_by = None  # To track who disliked the last film, so we don't repeat

# we can use a two pointer method to track the films they both want to watch
while i < n or j < m:
    if i < n and j < m and first_preferences[i] == second_preferences[j]:
        # Both like the same film on this day
        total += 1
        i += 1
        j += 1
        last_disliked_by = None  # Reset since both like the film
    elif i < n and (j >= m or first_preferences[i] < second_preferences[j]):
        # Emma likes the film, Marcos dislikes
        if last_disliked_by != 'Emma':  # Marcos cannot dislike two in a row
            total += 1
            last_disliked_by = 'Emma'
        i += 1
    elif j < m and (i >= n or second_preferences[j] < first_preferences[i]):
        # Marcos likes the film, Emma dislikes
        if last_disliked_by != 'Marcos':  # Emma cannot dislike two in a row
            total += 1
            last_disliked_by = 'Marcos'
        j += 1

print(total)
