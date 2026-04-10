class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recc(sub, count):
            if count==len(nums):
                ans.append(sub.copy())
                return

            sub.append(nums[count])
            recc(sub, count+1)
            sub.pop()
            recc(sub, count+1)

        recc([], 0)

        return ans


