# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        temp = []

        if root:
            q.append(root)
            q.append(None)
        else:
            return ans
        # q = 2 3 
        # temp = 
        while q:
            node = q.pop(0)
            if node==None:
                ans.append(temp)
                if len(q)>0:
                    q.append(None)
                temp = []
            else:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans
            

            







