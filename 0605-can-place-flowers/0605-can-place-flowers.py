class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        size = len(flowerbed)

        if size==1 and flowerbed[0]==0:
            flowerbed[0] = 1
            count+=1

        if size>1 and (flowerbed[0] == 0 and flowerbed[1]==0):
            flowerbed[0] = 1
            count += 1

        

        for i in range(1,size-1):

            if (flowerbed[i] == 0) and (flowerbed[i-1]==0 and flowerbed[i+1]==0):
                flowerbed[i] = 1
                count +=1

        if (size>1) and (flowerbed[size-1] == 0 and flowerbed[size-2]==0):
            flowerbed[size-1] = 1
            count+=1

        if count >= n:
            return True
        else:
            return False


        