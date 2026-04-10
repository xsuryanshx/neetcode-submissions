class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc+= str(len(i))+"#"+i
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        j = len(s)
        while i<j:
            k = i
            while s[k] != "#":
                k+=1
            length = int(s[i:k])
            dec.append(s[k+1:k+1+length])
            i=k+1+length
        return dec


        # print(s)
        # if len(s)<=2:
        #     return [s]
        # while s[j].isnumeric():
        #     print(s[j+2:j+2+int(s[j])])
        #     dec.append(s[j+2:j+2+int(s[j])])
        #     j+=2+int(s[j])
        #     if j>=len(s):
        #         break
        # return dec

    