class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        lower_index = 0
        high_index =  n-1       #   0,  n-1 =8  
        area =0
        while lower_index <= high_index:
            max_area = max(area, max_area)
            if height[lower_index] <= height[high_index]:
                area = (high_index - lower_index)*height[lower_index]
                lower_index+=1
            elif height[lower_index] >height[high_index]:
                area = (high_index - lower_index)*height[high_index]
                high_index-=1
        return max_area
            
        
    
            
            
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = (j-i)*min(height[i],height[j])
        #         if area > max_area:
        #             max_area =area
        # return max_area 

