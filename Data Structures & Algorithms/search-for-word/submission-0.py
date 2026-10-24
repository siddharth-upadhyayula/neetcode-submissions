from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int, index: int) -> bool:
            # Out of bounds or wrong character
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]
            ):
                return False

            # All characters have been matched
            if index == len(word) - 1:
                return True

            # Mark this cell as visited
            original = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r - 1, c, index + 1) or  # up
                dfs(r + 1, c, index + 1) or  # down
                dfs(r, c - 1, index + 1) or  # left
                dfs(r, c + 1, index + 1)     # right
            )

            # Restore the cell for other possible paths
            board[r][c] = original

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False