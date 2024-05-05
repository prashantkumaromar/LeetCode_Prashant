class Solution:
    def removeDuplicates(self, s: str) -> str:
#         stack =[] 
#         for i in s:
#             if not stack or stack[-1] == i:
        
#                 stack.append(i)
#             else:
#                 stack.pop()
#         return "".join(stack)

      
        stack = []        
        for c in s:
            stack.append(c) if (len(stack) == 0 or c != stack[-1]) else stack.pop()
        return ''.join(stack)
                
    
    
    
    
    
    
    
    
    # taking O(n^2), not optimized approach.
    # stack = []
        # for i in s:
        #     if i not in stack :
        #         stack.append(i)
        #     elif stack[-1] == i:
        #         stack.pop()
        #     elif stack[-1] != i and i in stack:
        #         stack.append(i)
        # return ''.join(stack)
                
            
            