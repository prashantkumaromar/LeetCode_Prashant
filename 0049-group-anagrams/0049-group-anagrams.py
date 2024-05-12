class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        
        for i in strs:
            alphabet_count = [0]*26
            for j in i:
                alphabet_count[ord(j)- ord('a')] += 1
            dict[tuple(alphabet_count)].append(i)           
        return dict.values()        







            #---------#broote force-------
        # sorted_lst =[]
        # res = []
        # dict = defaultdict(list)
        # for s in strs:
        #     sorted_lst.append(tuple(sorted(s)))
        
        # for i in set(tuple(sorted_lst)):
        #     for j in range(len(sorted_lst)):
        #         if i==sorted_lst[j]:
        #             dict[i].append(strs[j])
        #     res.append(dict[i])
        # return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                



            
