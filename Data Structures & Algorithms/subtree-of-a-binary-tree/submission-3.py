class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False
            return isSameTree(p1.left, p2.left) and isSameTree(p1.right, p2.right)

        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)