class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        for i in nums:
            p*=i
        ans = []

        for i,n in enumerate(nums):
            if n==0:
                copy = nums.copy()
                copy.pop(i)
                prod = 1
                for c in copy:
                    prod*=c
                ans.append(prod)
            else:
                ans.append(p//n)
        
        return ans
        