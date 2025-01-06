def permutation_Brute(arr, currentArr, visitArr, finalRes) -> None:
    if len(currentArr) >= len(arr):     # Base case ... when the currentArr.. contains the same length of elements as in input arr
        finalRes.append(currentArr.copy())
        return None
    
    else:
        # Traverse each element .. in the input arr
        for i in range(0, len(arr)):

            # Check the index of the element in input arr in visitedArr to find it is unvisited ..
            if visitArr[i] == False:

                # if unvisted then .. add it to the currentArr to generate permutions starting with the unvisited element
                currentArr.append(arr[i])

                # Mark the element as visited .. so that it doesn't need to be again added in permutation ..i,e currentArr
                visitArr[i] = True

                # Call this recursive function ... to get the remaing elements combinations
                permutation_Brute(arr, currentArr, visitArr, finalRes)

                # backtrack operations .. mark the current taken element as unmarked so that it can be added in another set of permutations
                visitArr[i] = False

                # remove the currently taken element from currentArr
                currentArr.pop()





def swap(arr, ind_1, ind_2):
    arr[ind_1], arr[ind_2] = arr[ind_2], arr[ind_1]


def permutation_Optimal(arr, pos_ind, finalRes) -> None:
    if pos_ind >= len(arr):     # Base case .. to return when the position passes the last index
        finalRes.append(arr.copy())
        return None
    
    else:
        # Traverse from the position index to the last index of input arr
        for ind in range(pos_ind, len(arr)):
            # Placing each element at respective position
            swap(arr, pos_ind, ind)

            # Perform same for the next position .. with the remaining elements
            permutation_Optimal(arr, pos_ind + 1, finalRes)

            # Backtrack operations ..  Place back the elements to maintain the previous state in input arr  - by swapping again
            swap(arr, pos_ind, ind)





lst = [5, 6, 7]

print("\n\n######################## Brute ############################")
visitArr = [False] * len(lst)
finalRes = []
currentArr = []
permutation_Brute(lst, currentArr, visitArr, finalRes)
print(finalRes)

print("\n\n######################## Optimal ############################")
finalRes_2 = []
permutation_Optimal(lst, 0, finalRes_2)
print(finalRes_2)