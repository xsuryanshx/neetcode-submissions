class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        r = n%2
        if n==1:
            return True
        if n<=0:
            return False
        if r==0:
            return self.isPowerOfTwo(n//2)
        else:
            return False