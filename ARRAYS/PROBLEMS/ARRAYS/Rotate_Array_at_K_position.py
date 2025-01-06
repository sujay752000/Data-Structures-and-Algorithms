class Solution:
    def reverse(self, arr, initial, final):
        while initial < final:
            arr[initial], arr[final] = arr[final], arr[initial]
            initial += 1
            final -= 1


    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)


lst = [1, 2, 3, 4, 5, 6, 7]
i = Solution()
i.rotate(lst, 3)
print(lst)