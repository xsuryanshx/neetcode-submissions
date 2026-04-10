class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_stack = []
        # i in tokens if tokens in [+-/*] then new_stack.pop() then append then push the last pop
        notations = ["+","-","/","*"]

        for tok in tokens:
            if tok in notations:
                num2 = new_stack.pop()
                num1 = new_stack.pop()
                if tok == "+":
                    new_stack.append(num1+num2)
                elif tok == "-":
                    new_stack.append(num1-num2)
                elif tok == "*":
                    new_stack.append(num1*num2)
                elif tok == "/":
                    new_stack.append(int(num1/num2))
            else:
                new_stack.append(int(tok))
            print(new_stack)
        
        return new_stack.pop()

            

