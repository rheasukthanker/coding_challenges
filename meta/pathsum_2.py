'''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root,targetsum,lst,results):
        if root.right==None and root.left==None:
            if targetsum-root.val==0:
                lst.append(root.val)
                results.append(lst)
        if root.right:
            self.helper(root.right,targetsum-root.val,lst+[root.val],results)
        if root.left:
            self.helper(root.left,targetsum-root.val,lst+[root.val],results)
        return results
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        return self.helper(root,targetSum,[],[])
