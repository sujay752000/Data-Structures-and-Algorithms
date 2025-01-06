from typing import List


class Solution:
    def minDays_Brute(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)

        if m * k > n:
            return -1
        
        def bouquets_Made(bloomDay, day, k):
            count = 0
            total_Bouquets = 0

            for i in range(0, len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    total_Bouquets += (count // k)
                    count = 0

            total_Bouquets += (count // k)
            return True if total_Bouquets >= m else False
            

        

        for i in range(1, max(bloomDay) + 1):

            if bouquets_Made(bloomDay, i, k):
                return i
            
        return -1
    


    def minDays_Optimal(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)

        if m * k > n:
            return -1
    
        def bouquets_Made(bloomDay, day, k, m, n):
            total_Bouquets = 0
            count = 0

            for i in range(0, n):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    total_Bouquets += (count // k)
                    count = 0

            total_Bouquets += (count // k)

            return True if total_Bouquets >= m else False



        high = float("-inf")
        low = float("inf")

        for day in bloomDay:
            high = max(high, day)
            low = min(low, day)

        ans = float("inf")
        while low <= high:

            mid = (low + high) // 2
            total_bouquets = bouquets_Made(bloomDay, mid, k, m, n)

            if total_bouquets:
                high = mid - 1
                ans = min(ans, mid)

            else:
                low = mid + 1


        return ans


                





S = Solution()
bloomDay = [3, 3, 2, 1, 1]
m = 2
k = 2
print(S.minDays_Brute(bloomDay, m, k))
print(S.minDays_Optimal(bloomDay, m, k))