# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = [(1,root)]
        while stack:
            current_depth, node = stack.pop()
            if node is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1,node.right))
                stack.append((current_depth+1,node.left))
        return depth