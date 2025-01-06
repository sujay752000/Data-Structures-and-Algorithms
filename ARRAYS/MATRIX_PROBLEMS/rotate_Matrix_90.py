import pprint
class Solution:
    def rotate_Brute(self, matrix: list[list[int]]) -> None:
        """_summary_ : Used a additional matrix.. and copied the elements in 90 deg rotated place

        Args:
            matrix (list[list[int]]): Input Matrix

        Returns:
            matrix (list[list[int]]): New Matrix rotated 90 deg clockwise

        Time and Space Complexity 
            Time : O(n * m)
            Space : O(n * m)
        """
        n = len(matrix)

        newMat = [[None for i in range(0, n)] for i in range(0, n)]

        for row in range(0, n):
            for col in range(0, n):
                newMat[col][(n - 1) - row] = matrix[row][col]

        return newMat
    

    def rotate_Optimal(self, matrix: list[list[int]]) -> None:
        """_summary_ : 1. Transpose = Anti Clockwise
                            traverse the matrix below the backward diagonal .. and swap the elements between two halfs .. sepaerated by diagonal
                            Now the matrix is in 90 deg Anti Clockwise.. but we want clockwise 90 degree
                       2. Reverse the colms in each row .. horizontally
        Args:
            matrix (list[list[int]]): Input Matrix

        Returns:
            matrix (list[list[int]]): Matrix rotated 90 deg clockwise

        Time and Space Complexity 
            Time : O(n * m) + O(n * m)
            Space : O(1)
        """

        # Transpose = Anti Clockwise
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # Reverse the colms in each row .. horizontally
        start_col = 0
        end_col = n - 1
        for row in range(0, n):
            while start_col < end_col:
                matrix[row][start_col], matrix[row][end_col] = matrix[row][end_col], matrix[row][start_col]
                start_col += 1
                end_col -= 1

            start_col = 0
            end_col = n - 1

        return matrix




S = Solution()
matrix = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]]

# O/P
# rot_mat = [[15, 13, 2, 5],
#             [14, 3, 4, 1],
#             [12, 6, 8, 9],
#             [16, 7, 10, 11]]

print("Input Matrix : \n")
pprint.pprint(matrix, width=20)


# print("\nResultant Matrix :  Brute Approach\n")
# pprint.pprint(S.rotate_Brute(matrix), width=20)


print("\nResultant Matrix :  Optimal Approach\n")
pprint.pprint(S.rotate_Optimal(matrix), width=20)
