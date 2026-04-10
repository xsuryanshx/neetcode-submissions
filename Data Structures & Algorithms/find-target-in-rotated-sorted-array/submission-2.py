class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        result = nums[0]
        min_i = 0

        while l<=r:
            m = (l+r)//2
            if nums[m] <= result:
                result = min(nums[m], result)
                min_i = m

            if nums[m] > nums[r]:
                l = m +1
            else:
                r = m-1

        print(min_i)

        if min_i == 0:
            l,r = 0, n-1
        elif target>=nums[0] and target<=nums[min_i-1]:
            l,r = 0, min_i-1
        else:
            l,r = min_i,n-1
        
        
        ans = -1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                ans = m
            if target > nums[m]:
                l = m+1
            else:
                r = m-1
        
        return ans

        
        