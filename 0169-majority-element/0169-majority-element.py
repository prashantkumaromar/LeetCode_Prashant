class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = nums[0]
        v =1
        
        for i in range(1,len(nums)):
            
                if nums[i] == a:
                    v+=1
                   
                elif nums[i] != a:
                    v-=1
                
                # elif v == 0:   you used this elif so it will be executed only if upper condition are flase but you need here to check for 3rd condition as well not just 1st or 2nd
                if v == 0:
                    a = nums[i]
                    v = 1
                
        return a

