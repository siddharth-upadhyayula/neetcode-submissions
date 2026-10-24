class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result=[]
        current=[]

        def backtrack(opencount, closecount):

            if opencount==n and closecount==n:
                result.append("".join(current))

            if opencount<n:
                current.append("(")
                backtrack(opencount+1,closecount)
                current.pop()

            if closecount<opencount:
                current.append(")")
                backtrack(opencount,closecount+1)
                current.pop()

        backtrack(0,0)

        return result