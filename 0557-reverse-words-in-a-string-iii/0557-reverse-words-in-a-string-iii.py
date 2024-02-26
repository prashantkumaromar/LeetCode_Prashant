from re import S

class Solution:
    def reverseWords(self, s: str) -> str:
    

        rev_list = []
        lst = s.split(' ')
        for words in lst:
            
            rev_list.append(''.join(list(words)[: : -1]))
            
        return (' '.join(rev_list))

                