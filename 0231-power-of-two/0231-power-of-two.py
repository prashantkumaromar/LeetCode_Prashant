class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n<=0:
        #     return False
        # elif math.floor(math.log2(n)) == math.log2(n):
        #     return True
        if n ==0:
            return False
        else:
            
            while n%2 ==0:
                n = n/2
            return n==1
            
        
        