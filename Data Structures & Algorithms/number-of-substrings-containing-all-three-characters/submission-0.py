class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for r in range(len(s)):
            last[s[r]] = r
            count += 1 + min(last['a'], last['b'], last['c'])
        return count