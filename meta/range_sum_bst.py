'''Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].'''
'''Time Complexity: O(N), where N is the number of nodes in the tree.

Space Complexity: O(N)

For the recursive and iterative implementations, we are performing a DFS (Depth-First Search) traversal. The recursive solution requires additional space to maintain the function call stack while the iterative solution requires additional space to maintain the stack. In both implementations, the worst-case scenario occurs when the tree is of chain shape, and we will reach all the way down to the leaf node. In this case, the space required for the stack is O(N).'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans

