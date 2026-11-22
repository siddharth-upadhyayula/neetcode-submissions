class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visited = {}
        final = 0
        l = 0
        max_freq=0
        for r in range(len(s)):
            visited[s[r]] = visited.get(s[r],0)+1
            max_freq = max(max_freq, visited[s[r]])

            if (r-l+1) - max_freq >k:
                visited[s[l]]-=1
                l+=1
            
            final=max(final, r-l+1)

        return final

                
            
            
            