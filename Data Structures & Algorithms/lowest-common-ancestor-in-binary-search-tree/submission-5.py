# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not self.exists(root, p.val):
            return None
        if not self.exists(root, q.val):
            return None

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

        return None

    def exists(self, root, value):
        curr = root

        while curr:
            if value == curr.val:
                return True
            elif value < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return False
            