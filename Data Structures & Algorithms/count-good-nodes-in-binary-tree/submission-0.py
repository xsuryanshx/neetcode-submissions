# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []
        def dfs(root, maxval):
            if root==None:
                return
            if root.val>=maxval:
                maxval = root.val
                good_nodes.append(maxval)

            dfs(root.left, maxval)
            dfs(root.right, maxval)

        dfs(root, float('-inf'))
        return len(good_nodes)