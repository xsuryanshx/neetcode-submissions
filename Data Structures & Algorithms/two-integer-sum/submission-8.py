class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            rem = target-nums[i]
            if nums[i] in d.keys() and d[nums[i]]!=i:
                return [d[nums[i]],i]
            d[rem] = i