############################################################### Approach 1 - Brute #########################################################

def nextElementSearch(nums, next_element):
    """_summary_ : Linear Search to findout the next element present or not

    Args:
        nums (list): array of elements
        next_element (int): element to find out (element + 1)

    Returns:
        bool: Boolean True if next_element exits or False if not
    """
    for element in nums:
        if element == next_element:
            return True

    return False


def longConsequtiveSequence_Brute(nums):
    """_summary_ = 1. Traverse the nums list and select each num
                   2. and check the next element exist in nums : using Linear Search
                        accordingly length is also incremented
                        step 2 continues till end of sequence

    Args:
        nums (list): array of elements

    Returns:
        int: Sequence length
    """
    ans = float("-inf")
    length = 0

    for element in nums:
        length = 1
        next_element = element + 1

        while nextElementSearch(nums, next_element):
            length += 1
            next_element += 1

        # till sequence the max of ans, length is taken
        ans = max(ans, length)
        # Set again length = 0 .. for next sequence
        length = 0

    return ans



############################################################### Approach 2 - Better #########################################################


def longConsequtiveSequence_Better(nums):
    """_summary_ : Sort the nums list first ... so the sequences get into a linear order
                   then if dudplicates .. elements found then we skip it .. by adding only length 1.. 
                   we will keep incrementing the length += 1 until the next element stops ... element + 1
                   if the next element is a far element then ... we will set the length = 1.. for next series calculation


    Args:
        nums (list): array of elements

    Returns:
        int: Sequence length
    """
    nums.sort()
    ans = float("-inf")
    length = 1
    element = nums[0]

    for i in range(1, len(nums)):

        if nums[i] == element:
            continue
        elif nums[i] == element + 1:
            length += 1
        else:
            length = 1

        ans = max(ans, length)
        element = nums[i]

    return max(ans, length)



############################################################### Approach 3 - Optimal #########################################################

def longConsequtiveSequence_Optimal(nums):
    """_summary_ : 1. Create a hashSet for nums .. (so lookup takes O(1) .. and also unique elements)
                   2. we first check if previous element .. (element - 1) present in hashSet .. if present then we skip .. and go for next element
                   3. if we get a element that has no previous element .. then actually it will be the starting sequence element..
                   4. so .. we will check the next element ..present in hashSet ...also incremnts the length += 1 accordingly .. 
                        this while loop keeps runnning until it reaches end of sequence

    Args:
        nums (list): array of elements

    Returns:
        int: Sequence length
    """
    ans = float("-inf")
    length = 0
    hashSet = set()

    # Creating a hashSet of nums =  O(n)
    for i in nums:
        hashSet.add(i)

    
    for element in hashSet:     # O(n)

        if element - 1 in hashSet:  # If previous element presents .. the we can avoid unnecessary look ups
            continue
        
        # This while() only starts with the begining of a sequence ...
        # because we only starts when the element doesn't have previous element in hashSet
        # This searching in hashSet takes .. only O(1)
        while(element in hashSet): # + O(n) not each time.. maximum this whole function goes = O(n) + o(n) + O(n) = O(3N)
            length += 1
            element = element + 1

        ans = max(ans, length)
        length = 0

    return max(ans, length)



# nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longConsequtiveSequence_Brute(nums))
print(longConsequtiveSequence_Better(nums))
print(longConsequtiveSequence_Optimal(nums))