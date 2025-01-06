class Solution:

    def inversionCount_Brute(self, arr):
        count = 0

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1

        return count



    def inversionCount(self, arr):

        def merge(arr, low, mid, high):
            count = 0

            temp = []
            i = low
            j = mid + 1

            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    count += j - (mid + 1)
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                count += j - (mid + 1)
                i += 1

            while j <= high:
                temp.append(arr[j])
                j += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

            return count

        def merge_Sort(arr, low, high):
            count = 0

            if low >= high:
                return count
            else:
                mid = (low + high) // 2

                count += merge_Sort(arr, low, mid)
                count += merge_Sort(arr, mid + 1, high)
                count += merge(arr, low, mid, high)
                return count

        return merge_Sort(arr, 0, len(arr) - 1)


S = Solution()
arr = [2, 4, 1, 3, 5, 2]
print(S.inversionCount_Brute(arr))
print(S.inversionCount(arr))