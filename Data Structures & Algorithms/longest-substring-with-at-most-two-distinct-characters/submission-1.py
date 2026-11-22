class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        final = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 
            while len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            final = max(final, r - l + 1)
        return final