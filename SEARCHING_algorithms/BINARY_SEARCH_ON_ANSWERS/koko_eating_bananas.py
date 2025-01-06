from math import ceil
from typing import List


class Solution:

    def minEatingSpeed_Brute(self, piles: List[int], h: int) -> int:

        def calTotal_Hours(k):
            total_hour = 0
            for pile in piles:
                total_hour += ceil(pile / k)

            return total_hour

        for i in range(1, max(piles) + 1):
            total_hour = calTotal_Hours(i)

            if total_hour <= h:
                return i

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calTotal_Hours(k):
            total_hour = 0
            for pile in piles:
                total_hour += ceil(pile / k)

            return total_hour

        maximum = max(piles)
        low = 1
        high = maximum
        res = float("inf")

        while low <= high:

            mid = low + (high - low) // 2

            total_hour = calTotal_Hours(mid)

            if total_hour <= h:
                res = min(res, mid)
                high = mid - 1

            else:
                low = mid + 1

        return ceil(maximum / h) if res == float("inf") else res


S = Solution()


piles = [3, 5, 6, 8, 7, 11]
h = 14
print(S.minEatingSpeed_Brute(piles, h))
print(S.minEatingSpeed(piles, h))