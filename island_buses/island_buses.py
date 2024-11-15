from collections import defaultdict, deque

def find_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_map = {}
    island_id = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        island_map[(r, c)] = island_id
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] in '#X':
                    visited.add((nr, nc))
                    island_map[(nr, nc)] = island_id
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in '#X' and (r, c) not in visited:
                bfs(r, c)
                island_id += 1

    return island_map, island_id

def find_bridges(grid, island_map, num_islands):
    rows, cols = len(grid), len(grid[0])
    visited_bridge = set()
    bridge_connections = set()

    def bfs_bridge(r, c):
        queue = deque([(r, c)])
        visited_bridge.add((r, c))
        endpoints = set()

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 'B' and (nr, nc) not in visited_bridge:
                        visited_bridge.add((nr, nc))
                        queue.append((nr, nc))
                    elif grid[nr][nc] in '#X' and (nr, nc) in island_map:
                        endpoints.add(island_map[(nr, nc)])

        # Add unique pairs of endpoints
        endpoints = list(endpoints)
        if len(endpoints) > 1:
            for i in range(len(endpoints)):
                for j in range(i + 1, len(endpoints)):
                    # Only add if the pair is not already added
                    bridge_connections.add(tuple(sorted((endpoints[i], endpoints[j]))))

    # Traverse all bridge cells to detect connections
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'B' and (r, c) not in visited_bridge:
                bfs_bridge(r, c)

    return list(bridge_connections)


def count_buses_needed(num_islands, bridges):
    if num_islands == 0:
        return 0
    if not bridges:
        return num_islands

    adj = defaultdict(list)
    for a, b in bridges:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()
    components = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)

    for island in range(num_islands):
        if island not in visited:
            components += 1
            dfs(island)

    return components

def process_map(grid, map_num):
    if not grid:
        print(f"Map {map_num}")
        print("islands: 0")
        print("bridges: 0")
        print("buses needed: 0")
        print()
        return

    island_map, num_islands = find_islands(grid)
    bridges = find_bridges(grid, island_map, num_islands)
    buses = count_buses_needed(num_islands, bridges)

    print(f"Map {map_num}")
    print(f"islands: {num_islands}")
    print(f"bridges: {len(bridges)}")
    print(f"buses needed: {buses}")
    print()

map_num = 1
current_map = []

try:
    while True:
        try:
            line = input().strip()
        except EOFError:
            if current_map:
                process_map(current_map, map_num)
            break

        if not line and current_map:
            process_map(current_map, map_num)
            map_num += 1
            current_map = []
        elif line:
            current_map.append(line)

except Exception as e:
    if current_map:
        process_map(current_map, map_num)
