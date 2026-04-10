class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()

        def recc(sub, rem):
            nonlocal ans
            if rem==0:
                ans.add(tuple(sorted(sub.copy())))
                return
            if rem<0:
                return 
            for i in range(len(nums)):
                sub.append(nums[i])
                recc(sub, rem-nums[i])
                sub.pop()
            
        recc([], target)
        return [list(i) for i in ans]

            
