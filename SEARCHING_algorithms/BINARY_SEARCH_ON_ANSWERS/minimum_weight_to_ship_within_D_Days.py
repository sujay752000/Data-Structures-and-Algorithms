from typing import List


class Solution:
    def shipWithinDays_Brute(self, weights: List[int], days: int) -> int:
        low = float("-inf")
        high = 0

        for weight in weights:
            low = max(low, weight)
            high += weight

        def weight_Possiblility(weights, min_weight, days):
            total_days = 1
            total_weight = 0

            for weight in weights:
                if (total_weight + weight) > min_weight:
                    total_days += 1
                    total_weight = weight

                else:
                    total_weight += weight

            return True if total_days == days else False
            

        for i in range(low, high + 1):
            if weight_Possiblility(weights, i, days):
                return i





    def shipWithinDays_Optimal(self, weights: List[int], days: int) -> int:
        low = float("-inf")
        high = 0

        for weight in weights:
            low = max(low, weight)
            high += weight

        def weight_Possiblility(weights, min_weight, days):
            total_days = 1
            total_weight = 0
            for weight in weights:
                if (total_weight + weight) > min_weight:
                    total_days += 1
                    total_weight = weight

                else:
                    total_weight += weight

            return True if total_days <= days else False



        while low <= high:
            mid = low + (high - low) // 2

            if weight_Possiblility(weights, mid, days):
                high = mid - 1
            else:
                low = mid + 1

        return low


S = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(S.shipWithinDays_Brute(weights, days))
print(S.shipWithinDays_Optimal(weights, days))