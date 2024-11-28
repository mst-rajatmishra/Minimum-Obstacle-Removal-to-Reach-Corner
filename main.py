import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize a 2D list to track the minimum obstacles removed to reach each cell
        # Start with infinity for all cells, except the starting point (0, 0)
        obstacles_removed = [[float('inf')] * n for _ in range(m)]
        obstacles_removed[0][0] = 0
        
        # Min-heap for BFS with the number of obstacles removed as priority
        # The heap stores tuples (obstacles_removed, x, y)
        pq = [(0, 0, 0)]  # Starting point with 0 obstacles removed
        
        while pq:
            # Get the current position and number of obstacles removed
            removed, x, y = heapq.heappop(pq)
            
            # If we've already visited this cell with fewer obstacles removed, skip it
            if removed > obstacles_removed[x][y]:
                continue
            
            # Check all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the number of obstacles to remove
                    new_removed = removed + grid[nx][ny]
                    
                    # If we found a path with fewer obstacles removed to reach (nx, ny)
                    if new_removed < obstacles_removed[nx][ny]:
                        obstacles_removed[nx][ny] = new_removed
                        heapq.heappush(pq, (new_removed, nx, ny))
        
        # The bottom-right corner will have the answer with the minimum obstacles removed
        return obstacles_removed[m-1][n-1]
