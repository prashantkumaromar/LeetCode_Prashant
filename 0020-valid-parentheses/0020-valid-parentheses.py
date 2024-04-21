class Solution:
    def isValid(self, s: str) -> bool:
        open_br = ["(", "[", "{"]
        close_br = [")", "]", "}"]
        paired = {"(": ")", "[":"]", "{":"}" }
        stack = []
        
        
        for i in s:
                if i in open_br:
                    stack.append(i)
                elif i in close_br:
                    if not stack:
                        return False
                    elif paired[stack[-1]] != i:
                        return False
                    elif i== paired[stack[-1]]:
                        stack.pop()
        if stack:
                return False
        else:
                return True
            
                
            
                    
                
        
                
                
                
        