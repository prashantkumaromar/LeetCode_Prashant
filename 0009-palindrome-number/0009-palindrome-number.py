class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x == 0:
            return True
        else:
            rev = 0
            for i in range(0, math.floor(math.log10(x))+1):
                rev = 10*rev + (x//(10**i))%10
                #  rev = 10*rev + (x//(10^i))%10 --you use df bitwise operator for power shit!
            return rev == x


                
        