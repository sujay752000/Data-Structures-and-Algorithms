class Solution:
    def matrixReshape_Approach1(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """_summary_ : New Matrix of size of r*c created and filled with None
                       used a col and row tracker variables to track the r and c of new matrix

        Args:
            mat (list[list[int]]): Input MATRIX
            r (int): no of rows of new matrix 
            c (int): no of cols of new matrix 

        Returns:
            list[list[int]]: Reshaped Matrix

        Time and Space:
            TC = New matrix + Input Matrix Traversal
                 O(m * n)   +  O(r * c)  ... both m*n and r*c are same
                 O(2(r * c))
                 O(r * c)

            SC = O(r * c) # if considering ans matrix
        """
        m = len(mat)
        n = len(mat[0])
        if n * m != r * c or m == r and n == c:
            return mat
        
        new_Mat = [[None for _ in range(0, c)] for _ in range(0, r)]       # New Matrix of size of r*c filled with None

        new_mat_row = 0
        new_mat_col = 0
        for row in range(0, m):
            for col in range(0, n):
                new_Mat[new_mat_row][new_mat_col] = mat[row][col]
                if new_mat_col < c - 1:
                    new_mat_col += 1
                else:
                    new_mat_col = 0
                    new_mat_row += 1

        return new_Mat
    


    def matrixReshape_Approach2(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """_summary_ : created a outer List .. and used a each_row : list to fill the row elements

        Args:
            mat (list[list[int]]): Input MATRIX
            r (int): no of rows of new matrix 
            c (int): no of cols of new matrix 

        Returns:
            list[list[int]]: Reshaped Matrix

        Time and Space:
            TC = Input Matrix Traversal
                 O(m * n)

            SC = O(r * c) # if considering ans matrix
        """
        m = len(mat)
        n = len(mat[0])
        if n * m != r * c or m == r and n == c:
            return mat
        
        new_Mat = []        # Outer List
        each_row = []       # Inner List ... inner row
        for row in range(0, m):
            for col in range(0, n):
                if len(each_row) < c:
                    each_row.append(mat[row][col])
                else:
                    new_Mat.append(each_row)
                    each_row = []
                    each_row.append(mat[row][col])

        if len(each_row) == c:
            new_Mat.append(each_row)

        return new_Mat
    


    def matrixReshape_Approach3(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """_summary_ : Used the position of each element .. if our new Matrix is legal to reshape ..i,e n * m == r * c
                       then the position of each element will be same in both matrix .. so, used the position to identify the 
                       respective row and col in new Matrix

        Args:
            mat (list[list[int]]): Input MATRIX
            r (int): no of rows of new matrix 
            c (int): no of cols of new matrix 

        Returns:
            list[list[int]]: Reshaped Matrix

        Time and Space:
            TC = New matrix + Position Traversal
                 O(r * c)   +  O(r * c)  ... both m*n and r*c are same
                 O(2(r * c))
                 O(r * c)


            SC = O(r * c) # if considering ans matrix
        """
        m = len(mat)
        n = len(mat[0])
        if n * m != r * c or m == r and n == c:
            return mat
        
        new_Mat = [[None for _ in range(0, c)] for _ in range(0, r)]

        for pos in range(0, r * c):
            new_Mat[pos // c][pos % c] = mat[pos // n][pos % n]

        return new_Mat







S = Solution()
mat = [[5, 10, 15, 20],
       [25, 30, 35, 40],
       [45, 50, 55, 60]]

# Reshape matrix parameters 
r = 6
c = 2
print("\nApproach 1 : \n")
print(S.matrixReshape_Approach1(mat, r, c))

print("\nApproach 2 : \n")
print(S.matrixReshape_Approach2(mat, r, c))

print("\nApproach 3 : \n")
print(S.matrixReshape_Approach3(mat, r, c))