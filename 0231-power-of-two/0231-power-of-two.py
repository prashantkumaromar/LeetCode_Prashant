class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       
    #1st soln  O(logn)
    # if n<=0:
        #     return False
        # elif math.floor(math.log2(n)) == math.log2(n):
        #     return True
        
        #2nd soln. O(logn)
#         if n ==0:
#             return False
#         else:
            
#             while n%2 ==0:
#                 n = n/2
#             return n==1

#--------Bitwise soln------------
        if n <=0:
            return False
        else:
            return n &- n == n
            
        
        