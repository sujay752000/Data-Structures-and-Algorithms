from collections import defaultdict, Counter
from typing import List


class Solution_Brute:

    def generate_row(self, row : int) -> List:
        """_summary_ = we know formula for finding current row coefficients/ elements:
                            row = n, col = k  =>  nC0 + nC1 + nC2 ... nCk

                            also nCr =              n!
                                        -----------------------------------
                                                r! * (n - r)!

                                                         n * n - 1 * n - 2 ...upto r times  (because common (n - r)! gets divided)
                            nCr can be reduced to =    -----------------------------------
                                                            1 * 2 * 3 .... upto r times   (helps in divisibility .. so that result does't get bigger)

                       Optimisation comes when we observe that .. the current element/coefficient
                                previous_result * (CURRENT_ROW - (current_col - 1))
                            =  -----------------------------------------------------
                                                current_col

        Args:
            row (int): current row 

        Returns:
            List: current row List with coefficients / elements

        Complexity:
            TC = O(n * n)
            SC = O(n) if considering
        """
        row_List = [1]
        for col in range(1, row + 1):

            res = 1
            for i in range(1, col + 1):
                res *= row - (i - 1)
                res //= i
            row_List.append(res)

        return row_List




    def generate(self, numRows: int) -> List[List[int]]:
        """_summary_ = Traverse from 0th row to numRows - 1 ... because pascals triangle's row and col starts from 0 .... Takes O(n)
                       call generate_row(row) .. to generate all rows elements ... and results a row_list ... Takes O(n * n)
                       Overal TC = O(n * n * n) = O(n^3)

        Args:
            numRows (int): _description_

        Returns:
            List[List[int]]: _description_

        Complexity:
            TC = O(n * n * n) = O(n^3)
            SC = O(1) , O(n * n) if considering
        """
        pascals_triangle = []

        for row in range(0, numRows):   # O(n)
            row_List = self.generate_row(row)   # O(n * n) ...O(n * n * n)
            pascals_triangle.append(row_List)

        return pascals_triangle




class Solution_Optimal:

    def generate_row(self, row : int) -> List:
        """_summary_ = we know formula for finding current row coefficients/ elements:
                            row = n, col = k  =>  nC0 + nC1 + nC2 ... nCk

                            also nCr =              n!
                                        -----------------------------------
                                                r! * (n - r)!

                                                         n * n - 1 * n - 2 ...upto r times  (because common (n - r)! gets divided)
                            nCr can be reduced to =    -----------------------------------
                                                            1 * 2 * 3 .... upto r times   (helps in divisibility .. so that result does't get bigger)

                       Optimisation comes when we observe that .. the current element/coefficient
                                previous_result * (CURRENT_ROW - (current_col - 1))
                            =  -----------------------------------------------------
                                                current_col

                            so, that we can avoid .. finding factorials.. which results in additional loop

                       

        Args:
            row (int): current row 

        Returns:
            List: current row List with coefficients / elements

        Complexity:
            TC = O(n)
            SC = O(n) if considering
        """
        row_List = [1]
        res = 1
        for col in range(1, row + 1):
            # current_element = (previous_res * (row - (col - 1))) // col
            res = res * (row - (col - 1))
            res = res // col
            row_List.append(res)

        return row_List


    def generate(self, numRows: int) -> List[List[int]]:
        """_summary_ = Traverse from 0th row to numRows - 1 ... because pascals triangle's row and col starts from 0
                       call generate_row(row) .. to generate all rows elements ... and results a row_list

        Args:
            numRows (int): _description_

        Returns:
            List[List[int]]: _description_

        Complexity:
            TC = O(n * n) = O(n^2)
            SC = O(1) , O(n * n) if considering
        """
        pascals_Triangle = []

        for row in range(0, numRows):   # O(n)

            row_List = self.generate_row(row)   # O(n) ... so O(n * n)
            pascals_Triangle.append(row_List)


        return pascals_Triangle



S = Solution_Optimal()
S2 = Solution_Brute()
numRows = 6
print(S.generate(numRows))
print(S2.generate(numRows))