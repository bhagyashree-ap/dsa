# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(left, right):

            #both empty
            if not left and not right:
                return True
            
            #either one is empty
            if not left or not right:
                return False
            
            #different vals
            if left.val != right.val:
                return False
            
            #check symmetry
            return (check(left.left, right.right) and check(left.right, right.left))

        return check(root.left,root.right)
        