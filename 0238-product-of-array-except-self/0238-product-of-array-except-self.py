class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left_arr = []
        right_arr = []
        lft_pro = 1
        right_pro = 1
        for i in range(len(nums)):
            # you used this in for i in range(len(nums)-1): u used len -1 while append need to be done len times
            left_arr.append(lft_pro)
            lft_pro *= nums[i]

        for j in range(len(nums)-1, -1,-1):
            #  here also same mistake- you used len -1      for j in range(len(nums)-1, 0,-1):

            right_arr.append(right_pro)
            right_pro *= nums[j]

        right_arr = reversed(right_arr)
        
        for i, j in zip(left_arr, right_arr):
           res.append(i*j)
        return res 
        