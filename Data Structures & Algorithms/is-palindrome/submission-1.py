import string 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        punct = string.punctuation
        s = "".join([i.lower() for i in s if i not in punct])
        print(s, len(s))
        if len(s)%2 ==0:
            print(s[:len(s)//2])
            print(s[len(s)//2:])
            return s[:len(s)//2] == s[len(s)//2:][::-1]
        else:
            print(s[:len(s)//2])
            print(s[len(s)//2+1:])
            return s[:len(s)//2] == s[len(s)//2+1:][::-1]