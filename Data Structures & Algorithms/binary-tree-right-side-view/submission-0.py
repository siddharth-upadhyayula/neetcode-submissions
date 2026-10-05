# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = 0
        res = []
        queue = deque([root])
        right=[]

        while queue:
            levelsize = len(queue)
            levels = []

            for r in range(levelsize):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                levels.append(current.val)
            rightnode = levels.pop()
            right.append(rightnode)
        return right
