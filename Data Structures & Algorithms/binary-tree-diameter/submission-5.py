# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = []
        heap = []
        def dfs(node):
            if node==None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            d.append(left+right)
            heapq.heappush(heap, -(left+right))

            return max(left,right)+1
        
        dfs(root)
        return -heap[0]
        
        


            

            

            

