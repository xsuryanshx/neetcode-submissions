from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        c = Counter(nums)
        sort_a = []
        sort_c = dict(sorted(c.items(), key=lambda i:i[1]))
        for key,val in sort_c.items():
            sort_a.append([key,val])
        count = k
        while count:
            ans.append(sort_a.pop()[0])
            count-=1

        return ans

                
