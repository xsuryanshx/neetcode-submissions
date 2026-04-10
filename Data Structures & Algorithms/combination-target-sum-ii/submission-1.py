class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        
        def dfs(i, sub, rem):
            if rem==0:
                ans.add(tuple(sub.copy()))
                return
            if i>=len(candidates) or rem<0:
                return
            
            sub.append(candidates[i])
            dfs(i+1, sub, rem-candidates[i])
            sub.pop()

            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, sub, rem)

        dfs(0,[],target)
        return [list(i) for i in ans]


            