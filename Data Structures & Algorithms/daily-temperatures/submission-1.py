class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temps = temperatures
        # res = [0]*len(temps)

        # stack = [[temps[0],0]]

        # for i, temp in enumerate(temps[1:]):
        #     while stack and stack[-1][0] < temp:
        #         ele, pos = stack.pop()
        #         res[pos] = i-pos+1
        #     stack.append([temp,i+1])
        #     print(stack)
        #     print(res)

        # return res

        n = len(temperatures)
        res = []

        for i in range(n):
            found=False
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    found = True
                    res.append(j-i)
                    break

            if not found:
                res.append(0)
                
        return res

            
            
        
        
                
