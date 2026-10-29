class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        
        # print(d)
        # print(d.items())
        # print(sorted(d.items(), key = lambda x:x[1]))
        ans = sorted(d.items(), key = lambda x:x[1])[-k:]
        return [i[0] for i in ans]

