def threeSumBrute(nums, n):
    hashSet = set()
    finalLst = []

    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    resList = [nums[i], nums[j], nums[k]]
                    resList.sort()

                    if tuple(resList) not in hashSet:
                        finalLst.append(resList)

                    hashSet.add(tuple(resList))

    return finalLst


def threeSumBetter(nums, n):
    hashMap = {}
    hashSet = set()
    finalList = []

    for i in range(1, n - 1):
        hashMap[nums[i - 1]] = i - 1

        for j in range(i + 1, n):
            twoSum = nums[i] + nums[j]
            rem = 0 - twoSum

            if rem in hashMap:
                resList = [nums[i], nums[j], rem]
                resList.sort()

                if tuple(resList) not in hashSet:
                    finalList.append(resList)

                hashSet.add(tuple(resList))

    return finalList


def threeSumOptimal(nums, n):
    finalList = []
    nums.sort()

    for i in range(0, n):
        """ when the current i index element eqauls to the previous i index ... then we keep incrementing the i until it gets different element"""
        if i != 0 and nums[i] == nums[i - 1]:   # when i is not the first index: not check for previous when i is the first index i,e 0
            continue

        j = i + 1   # j always i + 1 (next to i)
        k = n - 1   # k always the n - 1 element (last)

        while j < k:    # always takes the triplet when i , j , k are in sorted .. if it fails .. then we go for next i element
            threeSum = nums[i] + nums[j] + nums[k]

            if threeSum == 0:   # When threeSum == 0 .. we append the triplet list
                finalList.append([nums[i], nums[j], nums[k]])
                # increment the j and k until it gets a different element than its previous
                j += 1 # first increment then check for previous
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif threeSum < 0: # when threeSum < 0 : then i and k remains constant .. and j go for next element
                #increment the j until it gets a different element than its previous
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            else: # when threesum > 0 : then i and j remains constant .. and k go for next element
                #increment the k until it gets a different element than its previous
                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            
    return finalList




lst = [-1, 0, 1, 2, -1, -4]
print("\n******************Brute******************")
print(threeSumBrute(lst, len(lst)))

print("\n******************Better******************")
print(threeSumBetter(lst, len(lst)))


print("\n******************Optimal******************")
print(threeSumOptimal(lst, len(lst)))
