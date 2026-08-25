# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, l, r):

            #no node
            if not node:
                return True
            
            if l is not None and node.val<=l:  #left limit
                return False
            
            if r is not None and node.val>=r:   #right limit
                return False
            
            #check subtrees
            return (check(node.left, l, node.val) and check(node.right, node.val, r))
        
        return check(root, None, None)
        

            

        