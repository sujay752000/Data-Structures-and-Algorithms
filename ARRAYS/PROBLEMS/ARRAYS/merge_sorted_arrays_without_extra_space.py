class Solution:
    def merge_brute(self, nums1 : list[int], nums2 : list[int]) -> None:
        """_summary_ = uses an addition storage space

        Args:
            nums1 (list[int]): list of integers
            nums2 (list[int]): list of integers

        Time and Space Complexity : 
            Time : O(n + m) + O(n + m)
            Space : O(n + m)

        """

        i = 0; j = 0; k = 0
        n = len(nums1)
        m = len(nums2)
        nums3 = [0] * (m+n)
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1

            k += 1

        
        while i < n:
            nums3[k] = nums1[i]
            i += 1
            k += 1

        while j < m:
            nums3[k] = nums2[j]
            j += 1
            k += 1


        for i in range(0, m + n):
            if i < n:
                nums1[i] = nums3[i]
            else:
                nums2[i - n] = nums3[i]


    def merge_better(self, nums1 : list[int], nums2 : list[int]) -> None:
        """_summary_ : Swap the elements in a way that ..    TC = O(min(n, m))
                            smaller elements in Left array (nums1)
                            larger elements in Right array (nums2)

                       Sort both arrays .. to get back to ascending order  TC = O(n log n) + O(m log m)

        Args:
            nums1 (list[int]): list of integers
            nums2 (list[int]): list of integers

        Time and Space Complexity : 
            Time : O(min(n, m)) + O(n log n) + O(m log m)
            Space : O(1) , Constant
        """
        i = len(nums1) - 1
        j = 0


        while i >= 0 and j < len(nums2) and nums1[i] > nums2[j]:    #TC = min(m, n)
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i -= 1
            j += 1

        nums1.sort()    #TC = n log n
        nums2.sort()    #TC = m log m 
    





S = Solution()
nums1 = [1, 5, 9, 10, 15, 20]
nums2 = [2, 3, 8, 13]
print(nums1, nums2)

# S.merge_brute(nums1, nums2)
S.merge_better(nums1, nums2)
print(nums1, nums2)