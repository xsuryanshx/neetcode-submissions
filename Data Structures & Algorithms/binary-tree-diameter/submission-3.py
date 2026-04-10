# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        heap = []
        heights = []
        def maxh(root):
            if root==None:
                return 0
            maxl = maxh(root.left)
            maxr = maxh(root.right)
            heapq.heappush(heap, -(maxl+maxr))
            return max(maxl,maxr)+1

        maxh(root)
        return -heapq.heappop(heap)

        

