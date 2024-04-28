class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i == "+":
                val1 = int(stack.pop())
                val2 = int(stack.pop(-1))
                stack.append(val1 + val2)
           # I want to keep on doing this below in pop[-2] is wrong. pop(-2) is right.chutiye               #syntax sikh ja pahle
            # if i == "+":
            #     val1 = int(stack.pop())
            #     val2 = int(stack.pop[-2])
            #     stack.append[val1 + val2]   // ye bhi galat likha hai chutiye append() ye hota
            elif i == "*":
                val1 = int(stack.pop())
                val2 = int(stack.pop(-1))
                stack.append(val1 *val2)
            elif i ==  "-":
                val1 = int(stack.pop())
                val2 = int(stack.pop(-1))
                stack.append(val2 - val1)
            elif i ==  "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop(-1))
                stack.append(val2 / val1)
            
            else:
                stack.append(i)
        return int(stack[-1])
                
                