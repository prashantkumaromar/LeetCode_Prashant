class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if i not in stack :
                stack.append(i)
            elif stack[-1] == i:
                stack.pop()
            elif stack[-1] != i and i in stack:
                stack.append(i)
        return ''.join(stack)
                
            
            