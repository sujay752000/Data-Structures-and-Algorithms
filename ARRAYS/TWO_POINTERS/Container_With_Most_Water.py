class Solution:
    def maxAreaOptimal(self, height):
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            point1 = height[left]
            point2 = height[right]

            breadth = right - left
            length = min(point1, point2)
            currentArea = length * breadth

            area = max(area, currentArea)

            if point1 < point2:
                left += 1
            elif point1 > point2:
                right -= 1
            else:
                left += 1
                right -= 1

        return area
    

    def maxAreaBrute(self, height):

        area = float('-inf')

        for i in range(0, len(height) - 1):
            for j in range(i + 1, len(height)):
                point1 = height[i]
                point2 = height[j]

                breadth = j - i
                length = min(point1, point2)
                currentArea = length * breadth

                area = max(area, currentArea)


        return area




height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
S = Solution()
print(S.maxAreaOptimal(height))
print(S.maxAreaBrute(height))   
