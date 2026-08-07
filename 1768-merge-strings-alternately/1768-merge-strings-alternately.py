class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        res = ""
        i=0
        j=0
        while i<n1 and j<n2:  
            res += word1[i]
            i +=1
            res += word2[j]
            j += 1

        if i<n1:
            while i<n1:
                res += word1[i]
                i+=1
        else:
            while j<n2:
                res += word2[j]
                j+=1

       

        return res
                

            
            





        