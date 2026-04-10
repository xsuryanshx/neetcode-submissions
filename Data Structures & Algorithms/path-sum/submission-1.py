# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = []
        def pathsum(root, cost=0):
            if root==None:
                return 

            cost+=root.val

            if root.left is None and root.right is None:
                sums.append(cost)
                
            pathsum(root.left, cost)
            pathsum(root.right, cost)


        pathsum(root)
        print(sums)
        if targetSum in sums:
            return True
        return False

            