class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp = temperatures
        # temp = temp[::-1]
        # res = [0]*len(temp)

        # for i in range(1,len(temp)):
        #     prev = i-1
        #     while (temp[i]<temp[prev] and prev>=0):
        #         res[i]+=1
        #         prev-=1
        temps = temperatures
        res = [0]*len(temps)

        stack = [[temps[0],0]]

        for i, temp in enumerate(temps[1:]):
            while stack and stack[-1][0] < temp:
                ele, pos = stack.pop()
                res[pos] = i-pos+1
            stack.append([temp,i+1])
            print(stack)
            print(res)

        return res
            
            
        
        
                
