class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])

        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    queue.append((row,col))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            rows, cols = queue.popleft()

            for dr,dc in directions:
                nr, nc = rows+dr, cols+dc


                if(0 <= nr < r
                        and 0 <= nc < c
                        and grid[nr][nc]==2147483647):
                    grid[nr][nc]=grid[rows][cols]+1
                    queue.append((nr,nc))