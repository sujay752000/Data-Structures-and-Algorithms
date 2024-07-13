def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:

        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1


    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    
    for i in range(0, len(temp)):
        arr[low + i] = temp[i]




def merge_Sort(arr, low, high):

    if low < high:
        mid = (low + high) // 2

        merge_Sort(arr, low, mid)
        merge_Sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
