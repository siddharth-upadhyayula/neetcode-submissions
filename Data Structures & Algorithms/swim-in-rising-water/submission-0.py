import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = {(0,0)}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:

            time, row, col = heapq.heappop(heap)

            if row==n-1 and col==n-1:
                return time

            for dr, dc in directions:
                nr, nc = row+dr, col+dc

                if (
                    not (0 <= nr < n and 0 <= nc < n) or (nr,nc) in visited
                ):
                    continue

                visited.add((nr,nc))

                new_time = max(time, grid[nr][nc])

                heapq.heappush(heap,(new_time, nr, nc))
        return -1