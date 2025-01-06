class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        res_list = []
        n = len(matrix)
        m = len(matrix[0])

        top_row = 0; bottom_row = n - 1
        left_col = 0; right_col = m - 1

        while top_row <= bottom_row and left_col <= right_col:
            # left to right
            for col in range(left_col, right_col + 1):
                res_list.append(matrix[top_row][col])
            top_row += 1

            # top to bottom
            for row in range(top_row, bottom_row + 1):
                res_list.append(matrix[row][right_col])
            right_col -= 1

            # right to left
            if top_row <= bottom_row:
                for col in range(right_col, left_col - 1, -1):
                    res_list.append(matrix[bottom_row][col])
                bottom_row -= 1

            # bottom to top
            if left_col <= right_col:
                for row in range(bottom_row, top_row - 1, -1):
                    res_list.append(matrix[row][left_col])
                left_col += 1   # next spiral .. starts from next col

        return res_list






S = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# matrix = [[1, 2, 3]]

# matrix = [[1],
#           [2],
#           [3]]

print(S.spiralOrder(matrix))
