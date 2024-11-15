#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

# Chat link: https://chatgpt.com/share/6722e8fd-c2b0-800a-af58-fcf8b55d5aab

from collections import deque

# function to count how big the board would be IF we were to update for some color
def count_connected(board, origin_color, target_color, n):
    visited = [[False] * n for _ in range(n)]
    connected_component = []
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    # Step 1: Find the connected component of origin_color tiles connected to the origin
    # This loop gathers all tiles directly connected to the origin that share the same color (origin_color)
    while queue:
        x, y = queue.popleft()
        connected_component.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == origin_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    # Step 2: From the initial connected component, find all tiles connected via target_color
    # Initialize total_connected with the size of the origin's connected component
    total_connected = len(connected_component)
    queue = deque()
    for x, y in connected_component:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # add valid adjacent tiles to the queue, which we will BFS on in the following step
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == target_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    total_connected += 1

    # Step 3: Explore the remaining connected target_color tiles with BFS
    # This loop continues expanding the connected component of target_color tiles that are adjacent to the initial component
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == target_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    total_connected += 1

    return total_connected

# BFS function to update the current color to the new color throughout the board
def flood_fill(board, origin_color, target_color, n):
    # init for BFS, using queue
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        board[x][y] = target_color  # Change the color to target_color

        # loop through all possible moves, add to queue if not visited and wihtin range of board
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == origin_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# (naive) helper function to check if the board is totally filled
def all_tiles_same(board, n):
    color = board[0][0]
    for i in range(n):
        for j in range(n):
            if board[i][j] != color:
                return False
    return True

def simulate_game(board, n):
    move_count = 0
    color_frequency = [0] * 6  # Colors 1 to 6

    # continue to make moves on the board until the board is totally full
    while not all_tiles_same(board, n):
        origin_color = board[0][0]
        max_connected = -1
        best_color = None

        #loop through each color, then determine which color has the most updated
        for color in range(1, 7):
            if color != origin_color:
                connected = count_connected(board, origin_color, color, n)
                if connected > max_connected or (connected == max_connected and (best_color is None or color < best_color)):
                    max_connected = connected
                    best_color = color

        # Once we know which color has the most updates, lets perform the move
        flood_fill(board, origin_color, best_color, n)
        color_frequency[best_color - 1] += 1
        move_count += 1

    return move_count, color_frequency

test_cases = int(input())
for _ in range(test_cases):
    n_line = ''
    # Skip empty lines in input, process the rest of the unput
    while n_line.strip() == '':
        n_line = input()
    n = int(n_line)
    board = []
    for _ in range(n):
        row = input().strip()
        board.append([int(c) for c in row])
    
    #start game simulation
    move_count, color_frequency = simulate_game(board, n)
    
    # print output for given test case
    print(move_count)
    print(' '.join(str(freq) for freq in color_frequency))