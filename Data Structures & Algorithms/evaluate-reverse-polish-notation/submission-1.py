from functools import reduce
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = []

        for i in tokens:
            if i == '+':
                b = curr.pop()
                a = curr.pop()
                curr.append(a + b)
            elif i == "*":
                b = curr.pop()
                a = curr.pop()
                curr.append(a * b)
            elif i == "-":
                b = curr.pop()
                a = curr.pop()
                curr.append(a - b)
            elif i == "/":
                b = curr.pop()
                a = curr.pop()
                curr.append(int(a / b))
            else:
                curr.append(int(i))
        
        return curr[0]