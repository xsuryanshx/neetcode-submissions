from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        vocab = defaultdict(int)
        for r in range(len(s)):
            vocab[s[r]]+=1
            while r-l+1 - max(vocab.values()) > k:
                vocab[s[l]]-=1
                l+=1
            print(s[l:r])
            max_len = max(r-l+1, max_len)

        return max_len



