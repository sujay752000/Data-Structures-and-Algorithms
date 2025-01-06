from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n:
            newStart = newInterval[0]
            newEnd = newInterval[1]
            resInterval = []

            start_i = n
            low = 0
            high = n - 1


            while low <= high:
                mid = (low + high) // 2

                if intervals[mid][1] >= newStart:
                    start_i = mid
                    high = mid - 1
                else:
                    low = mid + 1



            if start_i == n:
                intervals.append(newInterval)
                return intervals
            
            elif intervals[start_i][0] > newEnd:
                resInterval.extend(intervals[0 : start_i]) 
                resInterval.append(newInterval)
                resInterval.extend(intervals[start_i : n])

                return resInterval
            
            else:
                end_j = 0
                low = start_i
                high = n - 1


                while low <= high:
                    mid = (low + high) // 2

                    if intervals[mid][0] <= newEnd:
                        end_j = mid
                        low = mid + 1
                    else:
                        high = mid - 1

                resInterval.extend(intervals[0 : start_i])

                resStart = min(newStart, intervals[start_i][0])
                resEnd = max(newEnd, intervals[end_j][1])

                resInterval.append([resStart, resEnd])

                resInterval.extend(intervals[end_j + 1 : n])


                return resInterval

                

        else:
            intervals.append(newInterval)
            return intervals
        



    def insert_Better(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        n = len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res




S = Solution()
intervals = [[1,2], [3, 5],  [6,7], [8,10], [14,16]]
newInterval = [4, 8]


intervals = [[1, 5]]
newInterval = [0, 0]

intervals = [[1,3],[6,9]]
newInterval = [2, 5]


intervals = [[2,5],[6,7],[8,9]]
newInterval = [0,1]

# intervals = [[1, 2], [7, 9], [11, 12]]
# newInterval = [5, 6]


print(S.insert(intervals, newInterval))
print(S.insert_Better(intervals, newInterval))