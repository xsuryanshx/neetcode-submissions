class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()

        def recc(start, sub, rem):
            nonlocal ans
            if rem==0:
                ans.add(tuple(sorted(sub.copy())))
                return
            if rem<0:
                return 
            for i in range(start, len(nums)):
                sub.append(nums[i])
                recc(i,sub, rem-nums[i])
                sub.pop()
            
        recc(0, [], target)
        return [list(i) for i in ans]

            
