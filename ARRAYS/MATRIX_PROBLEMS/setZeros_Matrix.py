
import pprint
class Solution:

    def setZeroes_Brute(self, matrix : list[list[int]]) -> list[list[int]]:
        """_summary_ : 1. new matrix is created to store the resultant matrix
                       2. traverse in input matrix ...
                       3. check the matrix[row][col] == 0 ... if 0 , then
                            1. set the respective row for all column elements = 0
                            2. set the respective colum for all rows = 0

        Args:
            matrix (list[list[int]]): input matrix

        Returns:
            list[list[int]]: matrix

        Time and Space Complexity 
            Time : O(n * m) + O(n * m) + O(n + m)
            Space : O(n * m)
        """
        n = len(matrix)
        m = len(matrix[0])
        newMat = [[None for i in range(0, m)] for i in range(0, n)] # O(n * m)

        def setRow_Zeros(row, newMat):
            for col in range(0, m):
                newMat[row][col] = 0

        def setCol_Zeros(col, newMat):
            for row in range(0, n):
                newMat[row][col] = 0

        for row in range(0, n):     # O(n)
            for col in range(0, m): # * O(m)
                if matrix[row][col] == 0:
                    setRow_Zeros(row, newMat)   # + O(m)
                    setCol_Zeros(col, newMat)   # + O(n)
                else:
                    if newMat[row][col] != 0:
                        newMat[row][col] = matrix[row][col]

        return newMat


    def setZeroes_Better(self, matrix : list[list[int]]) -> list[list[int]]:
        """_summary_ : 1. Create two hashSets ... 1. rowsHashSet, 2. colsHashSet => for storings rows , and cols that has zeros in them
                       2. Traverse in the matrix and identify the cell that has zero .. if a cell has zero..
                            2.1 then we will add the respective row in rowsHashSet
                            2.2 and also add the respective col in colsHashSet

                        3. Again traverse in the matrix .. and check the row and col exists in rowsHasSet or colsHashSet
                            3.1 if exits then we will set the cell = 0 .. i,e matrix[row][col] = 0

        Args:
            matrix (list[list[int]]): input matrix

        Returns:
            list[list[int]]: matrix

        Time and Space Complexity 
            Time : O(n * m) + O(n * m)
            Space : O(n + m)
        """
        rowsHashSet = set() 	#SC = O(n) when all unique rows
        colsHashSet = set()     #SC = O(m) when all unique cols

        n = len(matrix)
        m = len(matrix[0])

        for row in range(0, n):         # O(n)
            for col in range(0, m):     # * O(m)
                if matrix[row][col] == 0:
                    rowsHashSet.add(row)    #O(1)
                    colsHashSet.add(col)    #O(1)

        for row in range(0, n):     # O(n)
            for col in range(0, m): # * O(m)
                if row in rowsHashSet or col in colsHashSet:    #O(1)
                    matrix[row][col] = 0


        return matrix


    def setZeroes_Optimal(self, matrix : list[list[int]]) -> list[list[int]]:
        """_summary_ : 1. if a matrix cell has 0..
                        then we it will be marked in the respective matrix[row][0] .. first colm in respective row
                        and also the respective column is marked as 0 in the first row ..i,e matrix[0][col]

                        in short
                        The first cell of each row i,e => matrix[row][0] .. is used for rows updation flag ... by setting the cell with 0
                        The first cell of each colm i,e => matrix[0][col] ... is used for cols updation flag ... by setting the cell with 0

                       2. 
        Args:
            matrix (list[list[int]]): input matrix

        Returns:
            list[list[int]]: matrix

        Time and Space Complexity 
            Time : O(n * m) + O(n * m)
            Space : O(1)
        """
        n = len(matrix)
        m = len(matrix[0])

        # Handling the first row => 0th row ... because the first cell matrix[0][0] is intersecting ..between rows updation cells, and cols updation cells 
        first_row_change = False
        for col in range(0, m):         # traversing all cols for 1 st row
            if matrix[0][col] == 0:     # checking each cols for 1 st row
                first_row_change = True # if any col has zero .. then will update the first_row_change flag = True

        # Handling remaining rows .. 1 - to - n
        for row in range(1, n):
            for col in range(0, m):
                if matrix[row][col] == 0:   # if any cell = 0
                    matrix[row][0] = 0      # setting the first col => i,e 0th col , in respective row with = 0
                    matrix[0][col] = 0      # setting the respective col in the first row => i,e 0th row with = 0


        #setting cells with Zeros
        for row in range(n - 1, -1, -1):   # Traversing the rows from last .. because the first row => i,e 0th row contains the markings of cols that needs to set zero
            
            if row == 0:
                if first_row_change == True:
                    for col in range(m - 1, -1, -1):
                        matrix[row][col] = 0
            else:
                # Traversing the cols from last .. because if the first cell is marked in the 0th row as 0 .. then as a result the respective cell i,e ematrix[row][0] becomes 0
                # so, while checking matrix[0][col] or matrix[row][0] always gets true.. because we already done the matrix[row][0] ... so all the remaining elements sets to 0
                for col in range(m - 1, -1, -1):
                    if matrix[row][0] == 0 or matrix[0][col] == 0:
                        matrix[row][col] = 0


        return matrix




S = Solution()
matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]

print("Input Matrix : \n")
pprint.pprint(matrix, width=20)


# print("\nResultant Matrix :  Brute Approach\n")
# pprint.pprint(S.setZeroes_Brute(matrix), width=20)


# print("\nResultant Matrix :  Better Approach\n")
# pprint.pprint(S.setZeroes_Better(matrix), width=20)


print("\nResultant Matrix :  Optimal Approach\n")
pprint.pprint(S.setZeroes_Optimal(matrix), width=20)
