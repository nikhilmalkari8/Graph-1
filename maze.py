from collections import deque

def hasPath(maze, start, destination):
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([tuple(start)])
    visited = set()
    visited.add(tuple(start))
    
    while queue:
        x, y = queue.popleft()
        
        # If we reach the destination
        if [x, y] == destination:
            return True
        
        # Roll the ball in all directions
        for dx, dy in directions:
            nx, ny = x, y
            # Keep rolling until hitting a wall or boundary
            while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
            
            # If the new stop position is not visited, add to queue
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False
