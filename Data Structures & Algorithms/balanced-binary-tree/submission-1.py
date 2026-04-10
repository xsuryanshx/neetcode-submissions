# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node==None:
                return [0, True]

            lenL, balL = dfs(node.left)
            lenR, balR = dfs(node.right)
            
            if balL and balR and abs(lenL - lenR) <=1:
                res = True
            else:
                res = False  

            return [max(lenL,lenR)+1, res]

        return dfs(root)[1]
