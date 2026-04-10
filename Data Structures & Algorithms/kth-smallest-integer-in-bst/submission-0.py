# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def find(root):
            if root==None:
                return 
            
            if root.left:
                find(root.left)
            ans.append(root.val)
            if root.right:
                find(root.right)

        find(root)
        print(ans)
        return ans[k-1]
            


        