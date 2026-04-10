from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # d_s1 = defaultdict(int)
        # for i in s1:
        #     d_s1[i]+=1

        # d_s2 = defaultdict(int)

        # l = 0

        # for r in range(len(s2)):
        #     d_s1 = d_s1.copy()

        s1 = "".join(sorted(s1))
        k = len(s1)

        for i in range(len(s2)-k+1):
            sorted_substring = "".join(sorted(s2[i:i+k]))
            print(sorted_substring, s1)
            if sorted_substring == s1:
                return True
            
        return False

            
            

