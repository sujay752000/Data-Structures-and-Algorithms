from typing import List


class Solution:
    def trap_optimal(self, height: List[int]) -> int:
        """_summary_ = Uses two pointer approach, uses a left and right pointer for traversing, 
                       also uses a leftMax pointer which stores left max height
                       and a rightMax pointer which stores right max height

                       if leftMax <= rightMax then .. traverse from, left to right for collecting trapped water
                       elif rightMax < leftMax, then . traverse from, right to left for collecting trapped water


        Args:
            height (List[int]): array of integers that represents height of bars

        Returns:
            int: trapped water count

        Time and Space Analysis:
                TC = O(n)
                SC = O(1)
        """
        trappedWater = 0
        left = 0; leftMax = height[left]
        right = len(height) - 1; rightMax = height[right]

        while left < right:                     #TC = O(n), SC= O(1)
            if leftMax <= rightMax:
                # already know leftMax is minimum
                left += 1
                leftMax = max(leftMax, height[left]) # updating current leftMax to avoid negative value.. if height[left] is large
                trappedWater += leftMax - height[left] # if our height[left] is large .. then it will be our current leftMax .. so results 0 , instead of negative
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                trappedWater += rightMax - height[right]

        return trappedWater




    def trap_Brute(self, height: List[int]):
        """_summary_ = Hashed leftMax of each index in prefixMaxArr
                       Hashed rightMax of each index in postfixMaxArr
                       Traversed the height array ..
                        - and computed the leftMax, and rightMax of that respective index
                            leftMax = prefixMaxArr[i]
                            rightMax = postfixMaxArr[i]
                        - calculated the min(leftMax, rightMax)
                        - if our min(leftMax, rightMax) > height[i]:
                            trappedWater += min(leftMax, rightMax) - height[i]

        Args:
            height (List[int]): array of integers that represents height of bars

        Returns:
            int: trapped water count

        Time and Space Analysis:
                TC = O(n) + O(n) + O(n)
                   = O(3n)
                   = O(n)

                SC = O(n) + O(n)
                   = O(2n)
                   = O(n)
        """
        prefixMaxArr = [None] * len(height)         #SC = O(n)
        prefixMax = height[0]
        for i in range(0, len(height)):             #TC = O(n)
            prefixMaxArr[i] = prefixMax
            prefixMax = max(prefixMax, height[i])

        postfixMaxArr = [None] * len(height)        #SC = O(n)
        postfixMax = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):    #TC = O(n)
            postfixMaxArr[i] = postfixMax
            postfixMax = max(postfixMax, height[i])

        trappedWater = 0
        # first and last element can't hold water because both of them as no bounder on each side
        for i in range(1, len(height) - 1):         #TC = O(n)
            leftMax = prefixMaxArr[i]
            rightMax = postfixMaxArr[i]
            if min(leftMax, rightMax) > height[i]:
                trappedWater += min(leftMax, rightMax) - height[i]

        return trappedWater


S = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 3]
# height = [0, 5, 6, 4, 6, 1, 0, 0, 2, 7]

print("\n************************ BRUTE ************************")
print(S.trap_optimal(height))

print("\n************************ OPTIMAL ************************")
print(S.trap_Brute(height))
