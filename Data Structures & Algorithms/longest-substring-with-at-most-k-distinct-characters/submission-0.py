class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        final = 0
        l = 0

        for r in range(len(s)):

            count[s[r]]+=1
            while len(count)>k:
                count[s[l]]-=1

                if count[s[l]]==0:
                    del count[s[l]]

                l+=1

            final = max(final, r-l+1)

        return final