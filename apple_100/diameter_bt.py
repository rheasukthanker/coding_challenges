class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longest_path(node):
            if not node:
                return -1
            nonlocal diameter
            longest_right = longest_path(node.right)
            longest_left = longest_path(node.left)
            diameter = max(diameter,longest_right+longest_left+2)
            return max(longest_right,longest_left)+1

        longest_path(root)
        return diameter