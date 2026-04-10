class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        if len(s)<=1:
            return len(s)

        max_len = 0

        window = set(s[0])
        for r in range(1,len(s)):
            if s[r] not in window:
                window.add(s[r])
            else:
                while(s[r] in window):
                    window.remove(s[l])
                    l+=1
                window.add(s[r])
                
            max_len = max(max_len, r-l+1)

        return max_len
        