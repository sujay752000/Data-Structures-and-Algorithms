def partition(arr, low, high):
    pivot = arr[low]

    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] >= pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def sortColors(arr, low, high):

    if low < high:
        partitionIndex = partition(arr, low, high)
        sortColors(arr, low, partitionIndex - 1)
        sortColors(arr, partitionIndex + 1, high)

def sortColorsBetter(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(0, len(nums)):
        if nums[i] == 0:
            count_0 += 1

        elif nums[i] == 1:
            count_1 += 1

        else:
            count_2 += 1


    left = 0


    while left < count_0:
        nums[left] = 0
        left += 1

    while left < count_0 + count_1:
        nums[left] = 1
        left += 1

    while left < count_0 + count_1 + count_2:
        nums[left] = 2
        left += 1



def sortColorsDutchNationalFlagALgorithm(nums):

    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1



nums = [2, 0, 2, 1, 1, 0]
# nums = [2, 0, 1]
# sortColors(nums, 0, len(nums) - 1)
# sortColorsBetter(nums)
sortColorsDutchNationalFlagALgorithm(nums)

print(nums)