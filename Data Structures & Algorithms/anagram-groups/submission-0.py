class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        d = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word not in d.keys():
                d[sorted_word] = []
            
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            d[sorted_word].append(strs[i])
        
        return list(d.values())

