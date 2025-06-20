def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = True

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        current = stack.pop()

        if current == end:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current[0]][current[1]]
            return path[::-1]  # Reverse the path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and maze[nr][nc] == 0:
                    visited[nr][nc] = True
                    parent[nr][nc] = current
                    stack.append((nr, nc))

    return None  # No path found
