class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = []
        p = []
        z = []

        for i in nums:
            if i<0:
                n.append(i)
            elif i>0:
                p.append(i)
            else:
                z.append(i)

        answer = []
        if len(z)>=3:
            answer.append([0,0,0])
        if len(z)>0:
            for i in range(len(p)):
                if -p[i] in n:
                    answer.append([-p[i],0,p[i]])

        for i in range(len(p)):
            for j in range(len(n)):
                if -(p[i]+n[j]) in n[:j]+n[j+1:]:
                    combo = sorted([p[i], n[j], -(p[i]+n[j])])
                    answer.append(combo)

        for i in range(len(n)):
            for j in range(len(p)):
                if -(n[i]+p[j]) in p[:j]+p[j+1:]:
                    combo = sorted([n[i], p[j], -(n[i]+p[j])])
                    answer.append(combo)

        set_ans = set(tuple(i) for i in answer)
        return [list(i) for i in set_ans]