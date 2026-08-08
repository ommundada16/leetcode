class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        i=0
        j=n-1
        s_list = list(s)
        vowels = set("aeiouAEIOU")

        while i<j:

            while i<j and s_list[i] not in vowels:
                i+=1

            while i<j and s_list[j] not in vowels:
                j-=1

            if i<j:
                s_list[i],s_list[j] = s_list[j],s_list[i]
                i+=1
                j-=1



            


        return "".join(s_list) 

        #.join() is a built-in method called directly on a delimiter string. The delimiter specifies what character to place between each element when stitching them together.