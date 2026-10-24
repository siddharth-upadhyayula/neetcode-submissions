from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int) -> None:
            # The whole string has been partitioned
            if start == len(s):
                result.append(current.copy())
                return

            # Try every substring starting at `start`
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    current.append(s[start:end + 1])
                    backtrack(end + 1)
                    current.pop()  # Undo the choice

        backtrack(0)
        return result