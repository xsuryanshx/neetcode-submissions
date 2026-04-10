class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        if len(s)==0:
            return 0

        vocab = set()
        vocab.add(s[0])
        max_len = 1

        for r in range(1, len(s)):
            while s[r] in vocab:
                vocab.remove(s[l])
                l+=1
            max_len = max(r-l+1, max_len)
            vocab.add(s[r])

        return max_len           

                
            





        