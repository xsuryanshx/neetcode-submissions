# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, mini, high):
            if root==None:
                return True
            
            if root.val>mini and root.val<high:
                return check(root.left, mini, root.val) and check(root.right, root.val, high)
            else:
                return False            


        mini = float('-inf')
        high = float('inf')
        return check(root, mini, high)


