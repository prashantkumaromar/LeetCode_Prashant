
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # counter ={}
        # List_dupl =[]
        # for i, val in enumerate(nums):
        #     if val in counter:
        #         counter[val] +=1
        #         List_dupl.append(val)

        #     else:
        #         counter[val] =1
        # return List_dupl











        counter = {}
        for val in nums: 
            if val not in counter: 
                counter[val] =0
            counter[val] +=1
        result =[] 
        for val, count in counter.items(): 
            if count >1: 
                result.append (val) 
        return result 

