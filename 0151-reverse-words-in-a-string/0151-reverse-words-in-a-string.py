class Solution:
    def reverseWords(self, s: str) -> str:
        
        word = ""
        lst = []

        n = len(s)

        for i in range(n):

            if s[i] != " ":
                word += s[i]

            else:

                if len(word)!=0:
                    lst.append(word)
                    word = "" 

        if len(word)!=0:
            lst.append(word)

        # n2 = len(lst)
        # res =""
        # for i in range(n2-1,-1,-1):
        #     if i != 0:
        #         res += lst[i]
        #         res += " "
        #     else:
        #         res += lst[i]

        lst.reverse()



    

        return " ".join(lst)



        
