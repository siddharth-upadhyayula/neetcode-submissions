class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        path = 0
        def dfs(i, j):
            nonlocal path
            if (i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0):
                return 

            if grid[i][j] != 0:
                return

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                path += 1
                return

            grid[i][j] = -1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            grid[i][j] = 0

        if grid[0][0] == 0:
            dfs(0, 0)

        return path