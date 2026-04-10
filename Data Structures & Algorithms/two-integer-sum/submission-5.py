class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            pos[i]=target-nums[i]
        ans = []
        for kv in pos.items(): 
            if kv[1] in nums[:kv[0]]+nums[kv[0]+1:]:
                ans.append(kv[0])
                print(kv)
                break
        
        for i in range(len(nums)):
            if (nums[i] == target-nums[ans[0]]) and (i!=ans[0]):
                ans.append(i)
        
        return ans
