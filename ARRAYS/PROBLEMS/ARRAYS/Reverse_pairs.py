from typing import List


class Solution:
    def reversePairs_Brute(self, nums: List[int]) -> int:
        count = 0

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > (2 * nums[j]):
                    print(nums[i], nums[j], "=> index :", i, j)
                    count += 1

        return count



    def reversePairs_Optimal(self, nums: List[int]) -> int:

        
        def reverse_pairCount(nums, low, mid, high):
            count = 0
            i = low
            j = mid + 1
            
            while i <= mid:

                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid +  1)
                i += 1

            return count



        def merge(nums, low, mid, high):
            temp = []
            i = low
            j = mid + 1

            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]


        def merge_sort(nums, low, high):
            count = 0
            if low >= high:
                return count

            else:
                mid = (low + high) // 2

                count += merge_sort(nums, low, mid)
                count += merge_sort(nums, mid + 1, high)
                count += reverse_pairCount(nums, low, mid, high)
                merge(nums, low, mid, high)
                return count


        return merge_sort(nums, 0, len(nums) - 1)

S = Solution()
# nums = [1, 3, 2, 3, 1]
nums = [2, 4, 3, 5, 1, 2]
# nums = [5, 4, 3, 2, 1]
# nums = [-5, -5]
# nums = [2, 2, -2, -2, -2, 2]
print(S.reversePairs_Brute(nums))
print(S.reversePairs_Optimal(nums))
