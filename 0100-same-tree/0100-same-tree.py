# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #check if empty
        if not p and not q:
            return True

        #check if either one is empty
        if not p or not q:
            return False
        
        #different values
        if p.val != q.val:
            return False
        
        #recursion
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))