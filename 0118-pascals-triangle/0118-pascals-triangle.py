class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #commenting for trying why my recursion solution is not working.
#         if numRows ==1:
#             return [[1]]
#         elif numRows ==2:
#             return [[1],[1,1]]
#         elif numRows ==3:
#             return [[1], [1,1],[1,2,1]]
#         else:
            
#             output =[[1], [1,1],[1,2,1]]
#             row =[1,2,1]
        
#             for i in range(3, numRows):
#                 for j in range(i-1):
#                     #i= 4 range(3,4) => 3 ---- i = 3
#                     # j => 0,1
#                     # row[]
#                     # j =
#                     temp = copy.copy(row)
#                     temp[j+1] = output[-1][j]+ output[-1][j+1]
#                     temp.append(1)
#                 output.append(temp)
#             return output
        
                
                
                
            
        
        
        
       
        
   
         
        if numRows ==1:
            return [[1]]   
        elif numRows ==2:
            return [[1],[1,1]]
        else:
            previous_rows = self.generate(numRows-1)
            previous_row = previous_rows[-1]
            curr_row = [1]
            for j in range(len(previous_row)-1):
                
                curr_row.append(previous_row[j] + previous_row[j+1])
            curr_row.append(1)
            previous_rows.append(curr_row)
                
            return previous_rows
        
        
        
        
        
        
        #mine one first try
#         PascalList =[]
#         pascal_0 = [1]
#         pascal_1 = [1,1]
         
         
#         if numRows ==1:
#             return [[1]]   
#         elif numRows ==2:
#             return [[1],[1,1]]
#         else:
#             for j in range(len(self.generate(numRows-1)[-1])):
                
#                 PascalList[j+1] = self.generate(numRows-1)[-1][j] + self.generate(numRows-1)[-1][j+1]
#                 PascalList[j].append(1)
                
#             return PascalList
        
        
        
        
        
        
        
        
                       
        
        
        