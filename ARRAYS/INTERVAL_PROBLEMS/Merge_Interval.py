from typing import List

class Solution:


    def merge_1(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()            # O(N log N)
        n = len(intervals)

        res = []
        i = 0

        while i < n:                # O(N)
            element = intervals[i]
            # Place an element and check which all upcomings elements can be merged

            j = i + 1
            while j < n and element[1] >= intervals[j][0]:
                element[1] = max(element[1], intervals[j][1])
                j += 1

            # merged interval .. if possible .. else the current element interval
            res.append(element)
            i = j

        return res
    


    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]   # at first we will add the first interval in res

        for i in range(1, len(intervals)):    # start from index 1

            currentInterval_Start = intervals[i][0]
            currentInterval_End = intervals[i][1]

            prevInterval_End = res[-1][1]

            if prevInterval_End >= currentInterval_Start:
                res[-1][1] = max(prevInterval_End, currentInterval_End)
            else:
                res.append([currentInterval_Start, currentInterval_End])

        return res

        

S = Solution()
intervals = [[1, 3], [8, 10], [2, 6], [3, 4], [15, 18], [8, 9], [8, 8]]
print(S.merge_1(intervals)) 
print(S.merge_2(intervals)) 