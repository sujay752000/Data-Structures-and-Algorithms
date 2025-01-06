from typing import List


class Solution:
    def findKthPositive_Brute(self, arr: List[int], k: int) -> int:     #TC = O(n) SC = (n)
        hashSet = set(arr)
        pos = 0
        for i in range(1, arr[-1] + k + 1):

            if i not in hashSet:
                pos += 1

            if pos == k:
                return i


    def findKthPositive_Better(self, arr: List[int], k: int) -> int:    #TC = O(n) SC = O(1)
        if k < arr[0]:
            return k

        for num in arr:
            if k >= num:
                k += 1
            else:
                return k
            
        return k
    




    def findKthPositive_Optimal(self, arr: List[int], k: int) -> int:      #TC = O(log n) SC = O(1)
        if k < arr[0]:
            return k
        
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            current_element = arr[mid]
            orginal_element = mid + 1
            missing_elements = current_element - orginal_element

            if missing_elements < k:
                low = mid + 1

            else:
                high = mid - 1


        current_element = arr[high]
        orginal_element = high + 1
        missing_elements = current_element - orginal_element
        remaining_elements = k - missing_elements

        return current_element + remaining_elements
    


S = Solution()
arr = [1, 2, 3, 4]
k = 2
print(S.findKthPositive_Brute(arr, k))
print(S.findKthPositive_Better(arr, k))
print(S.findKthPositive_Optimal(arr, k))
