"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyNode={None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyNode[cur]=copy
            cur = cur.next

        cur = head
        while cur:
            copy = copyNode[cur]
            copy.next = copyNode[cur.next]
            copy.random = copyNode[cur.random]
            cur = cur.next

        return copyNode[head]
