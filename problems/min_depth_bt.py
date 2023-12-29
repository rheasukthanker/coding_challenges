class Solution:
    def minDepth(self,root)->int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left=self.minDepth(root.left) if root.left else float('inf')
        right=self.minDepth(root.right) if root.right else float('inf')

        return 1+min(left,right) 
