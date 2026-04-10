class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        if len(s)==0:
            return 0

        vocab = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in vocab:
                vocab.remove(s[l])
                l+=1
            vocab.add(s[r])
            max_len = max(r-l+1, max_len)

        return max_len           

                
            





        