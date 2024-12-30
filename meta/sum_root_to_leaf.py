'''You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.'''
'''Complexity Analysis

Time complexity: O(N) since one has to visit each node.

Space complexity: up to O(H) to keep the recursion stack, where H is a tree height.'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def preorder(r: TreeNode, curr_number: int) -> None:
            nonlocal root_to_leaf
            if r:
                curr_number = curr_number * 10 + r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number

                preorder(r.left, curr_number)
                preorder(r.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
