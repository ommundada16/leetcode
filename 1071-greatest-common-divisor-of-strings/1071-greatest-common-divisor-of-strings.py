class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # freq = [0]*26

        # str1_len = len(str1)
        # str2_len = len(str2)

        # n = min (str1_len, str2_len)

        # res=""

        # for i in range(n):

        #     if str1[i] != str2[i]:
        #         break

        #     if (str1[i] == str2[i]) and freq[ord(str1[i])-ord('A')]==1:
        #         break
                
        #     if (str1[i] == str2[i]) and (freq[ord(str1[i])-ord('A')]==0):
        #         freq[ord(str1[i])-ord('A')]=1
        #         res += str1[i]

            

        # return res

        if str1 + str2 != str2 + str1:
            return ""

        def gcd_len(a, b):
            while b!=0:
                a , b = b , a%b

            return a


        n1 = len(str1)
        n2 = len(str2)

        length = gcd_len(n1,n2)

        return str1[:length]