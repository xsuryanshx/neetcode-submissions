class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        z_c = 0
        for i in nums:
            if i:
                p*=i
            else:
                z_c +=1
        ans = []
        if z_c>1:
            ans = [0]*len(nums)
            return ans
    

        for i,n in enumerate(nums):
            if z_c==1:
                ans.append(0 if n!=0 else p)
            else:
                ans.append(p//n)
        
        return ans
        