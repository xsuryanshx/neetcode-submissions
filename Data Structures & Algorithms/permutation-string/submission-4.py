from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # d_s1 = defaultdict(int)
        # for i in s1:
        #     d_s1[i]+=1

        # d_s2 = defaultdict(int)
        if len(s1)>len(s2):
            return False

        l = 0

        parity = [0]*26

        for c in s1:
            parity[ord(c)-ord('a')]+=1
        
        parity_c = parity[:]
        # print(parity_c)

        for r in range(len(s2)):
            l = r
            parity = parity_c.copy()
            # print("r", r, "l", l)
            while l<len(s2) and parity[ord(s2[l])-ord('a')] >=1:
                parity[ord(s2[l])-ord('a')]-=1
                # print("new parity",s2[l],parity)
                l+=1
            if sum(parity) == 0:
                return True

        return False
            





        # s1 = "".join(sorted(s1))
        # k = len(s1)

        # for i in range(len(s2)-k+1):
        #     sorted_substring = "".join(sorted(s2[i:i+k]))
        #     print(sorted_substring, s1)
        #     if sorted_substring == s1:
        #         return True
            
        # return False

            
            

