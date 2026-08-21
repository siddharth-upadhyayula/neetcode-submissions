# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        def dfs(node, height):
            if not node:
                return height

            left = dfs(node.left, 1+height)
            right = dfs(node.right, 1+height)

            res = max(left, right)

            return res

        return dfs(root, height)