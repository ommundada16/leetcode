class Solution:

    # def check_max(self,):


    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n= len(candies)
        res = []
        largest = max(candies)

        for i in range(n):

            if candies[i] + extraCandies >= largest:
                res.append(True)
            else:
                res.append(False)

        return res


