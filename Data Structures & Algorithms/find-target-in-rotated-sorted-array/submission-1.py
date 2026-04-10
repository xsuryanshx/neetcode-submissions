class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

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

        m = min_i
        l , r = 0 , len(nums)-1

        ans = -1

        while l <= r:
            if target == nums[m]:
                ans = m
            if target > nums[r]:
                r = m-1
            else:
                l = m+1
            m = (l+r)//2

        return ans

        
        