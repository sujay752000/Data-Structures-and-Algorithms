class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()     # Will add Sum of each squares of digits
        sumNum = 0

        while n:

            while n > 0:
                rem = n % 10
                n = n // 10
                sumNum += (rem * rem)


            if sumNum == 1:
                return True
            if sumNum in hashSet:      # if the sum .. i,e sumNum present in the hashSet then .. will return False
                # because .. it will fall in loop or circle .. because ..same the sumNum will generate .. the sum over and over
                return False
            
            hashSet.add(sumNum)
            n = sumNum
            sumNum = 0
    

n = 2
s = Solution()
print(s.isHappy(n))