class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        ans = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }


        for i in s:
            if i not in ans:
                stack.append(i)
                continue
            if not stack or stack[-1]!=ans[i]:
                return false
            
            stack.pop()
        return not stack
                   


