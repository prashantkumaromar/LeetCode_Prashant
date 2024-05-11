class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        product = 0
        lst =[]
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            product = product^nums[i]
        set_bit = product & -product   
        for j in range(len(nums)):
            if nums[j]& set_bit ==0:
            #  you wrote this -----if nums[j]& 1 ==0:    this is wrong -- we need set-bit(right most 1 of product)
                num1 = num1 ^ nums[j]
                
            else:
                num2 = num2 ^ nums[j]
        lst.append(num1^product)
        lst.append(num2^product)

        return lst


                

        


