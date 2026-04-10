class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ds = {}
        dt = {}
        for i in s:
            if i in ds.keys():
                ds[i]+=1
            else:
                ds[i]=1

        for i in t:
            if i in ds.keys():
                ds[i]-=1
                if ds[i]==0:
                    del ds[i]
            else:
                return False

        return True