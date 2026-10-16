class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return is_pal(i + 1, j) or is_pal(i, j - 1)
        return True