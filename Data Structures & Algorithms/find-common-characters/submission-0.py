from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = Counter(words[0])
        for i in range(1,len(words)):
             current = Counter(words[i])
             result = result & current
        return list(result.elements())
