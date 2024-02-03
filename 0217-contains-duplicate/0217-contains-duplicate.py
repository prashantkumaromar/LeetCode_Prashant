class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter ={}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i]+=1
        for  val, count in counter.items():
            
            if count >=2:
                return True
        return False
