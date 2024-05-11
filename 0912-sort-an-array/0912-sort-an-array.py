class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mid = n//2
        lst = n-1
        st = 0
        res = [0]*n
        idx1 =0
        idx2 =0
        r = 0
        
        if len(nums) ==1:
            return nums 
        else:
            l1 = self.sortArray(nums[: mid])
            l2 = self.sortArray(nums[mid :])
        while idx1 <len(l1) and  idx2 <len(l2):
            
            if l1[idx1] <= l2[idx2]:
                    res[r] = l1[idx1]

                    idx1+=1
            elif l2[idx2] <= l1[idx1]:
                    res[r] = l2[idx2]
                    idx2+=1
            r+=1
        while idx1 < len(l1):
            res[r] = l1[idx1]
            r+=1
            idx1+=1
        while idx2 < len(l2):
            res[r] = l2[idx2]
            r+=1
            idx2+=1    
        # elif l2:
        #     res.extend(l2[idx2:])
        # #res.append(l2[idx2:]). you previously wrote this instead of extend
        return res





