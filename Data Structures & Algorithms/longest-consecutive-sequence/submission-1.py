class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        answer = []
        max_len = 0

        print("sorted:", nums)
        if len(nums)<=1:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                print(nums[i])
                if nums[i+1]-nums[i]==1:
                    answer.append(nums[i])
                    print(answer)
                    if len(answer) > max_len:
                        max_len = len(answer)
                else:
                    answer = []
        return max_len+1
