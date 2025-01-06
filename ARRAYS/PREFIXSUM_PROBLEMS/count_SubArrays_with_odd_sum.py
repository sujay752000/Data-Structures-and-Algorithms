def subArrayCountBrute(arr, n):
    count = 0
    for i in range(0, n):
        prefixSum = 0
        for j in range(i, n):
            prefixSum += arr[j]

            if prefixSum % 2 != 0:
                count += 1

    return count


""" concept = if prefixSum upto an index = odd : .. then we increent the count + 1.. and will also add no of even summed prefix
                    : meaning when prefixSum is odd.. then each even summed prefix sub array is subtracted .. so that current prefixSum will always results a odd summed sub array

              if pefixSum upto an index = even .. then we will add no of odd summed prefix
                    : meaning when prefixSum is even .. then each odd summewd prefix sub array is subtracted .. so that current prefixSum will always results a odd summed sub array


    in short :
            prefixSum = odd : ansCount += 1
                              ansCount + no_of_even_prefixSum

            
            prefixSum = even : ansCount + no_of_odd_prefixSum

"""

def subArrayCountOptimal(arr, n):
    ansCount = 0
    evenPrefixSumCount = 0
    oddPrefixSumCount = 0
    prefixSum = 0

    for i in range(0, n):
        prefixSum += arr[i]

        if prefixSum % 2 == 0:
            ansCount += oddPrefixSumCount
            evenPrefixSumCount += 1
        else:
            ansCount += 1
            ansCount += evenPrefixSumCount
            oddPrefixSumCount += 1

    return ansCount


def subArrayIndexsOptimal(arr, n):
    oddPrefixSum = {}
    evenPrefixSum = {}
    prefixSum = 0
    finalList = []

    for i in range(0, n):
        prefixSum += arr[i]

        if prefixSum % 2 != 0:
            finalList.append([0, i])

            for sum in evenPrefixSum:
                finalList.append([evenPrefixSum[sum] + 1, i])

            oddPrefixSum[prefixSum] = i

        else:
            for sum in oddPrefixSum:
                finalList.append([oddPrefixSum[sum] + 1, i])

            evenPrefixSum[prefixSum] = i


    for i in finalList: #actual sub array
        print(arr[i[0] : i[1] + 1])

    
    return finalList    #indexes



lst = [1, 2, 3, 4, 5, 6, 7]
print("\n******************Brute Approach******************")
print(subArrayCountBrute(lst, len(lst)))

print("\n\n******************Optimal Approach******************")
print(subArrayCountOptimal(lst, len(lst)))

print("\n\n******************Optimal Approach******************")
print(subArrayIndexsOptimal(lst, len(lst)))