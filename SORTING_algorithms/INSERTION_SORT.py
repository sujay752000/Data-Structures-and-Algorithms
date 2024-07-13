def insertion_Sort(arr, n):
    """_summary_ = sorting algorithm that works by,
                   iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.

                    like sorting playing cards in your hands.
                    You split the cards into two groups: the sorted cards and the unsorted cards.
                    Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

    Args:
        arr (list): Array of elements
        n (int): length of array
    """
    for i in range(0, n):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:

            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


lst = [12, 3, 6, 5, 1, 4]
insertion_Sort(lst, len(lst))
print(lst)


"""_summary_ = Time and Space Complexity

    TC = Best =  O(n)
         Avg  =  O(n^2)
         Worst = O(n^2)

    SC = O(1)

    
    _Additionals_

    In-place = Yes, its a in-place alogo, beacuse it doesn't uses additional temporary space to sort array
    Stablity = Yes, it keeps relative oreder of equal elements in array
"""