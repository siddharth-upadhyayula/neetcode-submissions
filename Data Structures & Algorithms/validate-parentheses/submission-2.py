class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', '}':'{', ']':'['} # ) -> (
        stack = []

        for i in range(len(s)):
            if s[i] in map:
                if not stack or stack[-1]!=map[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])


        return not stack

