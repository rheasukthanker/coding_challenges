'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev):
            val = str(node.val)
            if not node.left and not node.right:
                self.sum += int(prev + val)
            if node.left:
                dfs(node.left, prev + val)
            if node.right:
                dfs(node.right, prev + val)
        
        self.sum = 0
        dfs(root, '')
        return self.sum
