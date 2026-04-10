class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        d = {"{": "}", "[":"]", "(":")"}
        stack = []
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif len(stack)>0 and d[stack[-1]] == i:
                stack.pop()
            else:
                return False

        return len(stack)==0

        



        



