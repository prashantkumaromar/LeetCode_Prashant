class MinStack:
    
    def __init__(self):
        self.stack = []
        self.Minstack = []

    def push(self, val: int) -> None:
                                        # min = +float(inf)
            self.stack.append(val)
            if not self.Minstack:
                self.Minstack.append(val)
            elif val <= self.Minstack[-1]:
                self.Minstack.append(val)
          
            
            
            
        
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.Minstack[-1] == val:
                self.Minstack.pop()
        
                
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        # if not self.Minstack:
        #     return -1
        # else:
            return self.Minstack[-1]
        
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()