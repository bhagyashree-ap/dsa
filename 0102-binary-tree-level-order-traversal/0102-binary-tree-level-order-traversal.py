# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#for level order (BFS):
#LC: 2i+1
#RC: 2i+2

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans=[]
        level=[root]

        while level:
            ans.append([node.val for node in level])    #curr level

            next_level=[]

            #if child node exists, append it to next level    
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level=next_level
        
        return ans




