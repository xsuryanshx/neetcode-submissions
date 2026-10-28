class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [ord(i) for i in s]
        t = [ord(i) for i in t]

        s = sorted(s)
        t = sorted(t)

        if s==t:
            return True
        else:
            return False
        