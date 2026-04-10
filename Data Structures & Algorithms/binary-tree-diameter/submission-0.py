# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = []
        def maxh(node):
            if node==None:
                return 0
            max_l = maxh(node.left)
            max_r = maxh(node.right)
            height.append(max_l+max_r)
            return max(max_l,max_r)+1

        maxh(root)
        return max(height)
