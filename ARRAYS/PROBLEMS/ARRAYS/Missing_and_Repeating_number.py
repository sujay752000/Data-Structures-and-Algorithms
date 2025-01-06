class Solution:

    def findTwoElement_Brute(self, arr):
        n = len(arr)
        repeat = -1
        missing = -1

        for i in range(1, n + 1):
            count = 0

            for num in arr:
                if i == num:
                    count += 1

            if count == 2:
                repeat = i

            if count == 0:
                missing = i

            if missing != -1 and repeat != -1:
                return [repeat, missing]




    def findTwoElement_Better(self, arr):
        """_summary_ = Mark the index position of numbers from 1 to n with its count
                       if count == 2, means the number is repeatng
                       if count == 0, then number is missing

        Args:
            arr (_type_): list of integers

        Returns:
            _type_: List[int, int] => [repeat, missing]

        Time and Space:
            Time : O(2n) => O(n)
            Space : O(n)
        """

        n = len(arr)
        repeat = None
        missing = None

        Total = (n * (n + 1)) // 2
        current_Total = 0

        series_arr = [0] * (n + 1)    # TC = O(n), and SC = O(n)
        
        for num in arr:             # TC =  O(n)
            current_Total += num

            series_arr[num] += 1

            if series_arr[num] == 2:
                repeat = num


        missing = Total - (current_Total - repeat)

        return [repeat, missing]




    def findTwoElement_Optimal(self, arr):
        """_summary_ : Solving by equation cocept
                       Total_Sum_N - Current_Sum = Value1
                            i,e 
                                Misising - Repeat = Value1   ---> eqn1

                       here we need to get two unknown variables .. so use eqautio to solve
                       i,e we need to find :  Missing + Repeat = Value2, so

                       Total_Sum_N_Square - Current_Sum_Square = Value2
                            i,e 
                                (Miising)^2 - (Repeat)^2 = value2   => ( Missing + Repaeat ) * ( Missing - Repeat ) = Value2
                            so, Missing + Repeat = value2 / (Missisng - Repeat)
                                Missing + Repeat = value2 / value1

                                Missing + Repeat = value2   ---> eqn2


                        So, from eqn 1 and eqn 2, we can find Missing number
                            Misising - Repeat = Value1   ---> eqn1
                            Missing + Repeat = value2   ---> eqn2

                        i,e      2 Missing = Value1 / Value2
                                 Missing = (Value1 / Value2) // 2


                        after getting Missing number, we can calculate Repeating number from either eqn 1 or eqn 2
                        i,e       Missing + Repeat = value2 
                                  Repeat = value2 - Missing

                        return [Repeat, Missing]

                                                

        Args:
            arr (_type_): list of integers

        Returns:
            _type_: List[int, int] => [repeat, missing]

        Time and Space:
            Time : O(n)
            Space : O(1)
        """
        n = len(arr)
        missing = -1
        repeat = -1

        total_N = (n * (n + 1)) // 2
        total_Current = 0

        total_Sqr_N = (n * (n + 1) * (2 * n + 1)) // 6
        total_Current_Sqr = 0

        for num in arr:
            total_Current += num
            total_Current_Sqr += num * num

        val1 = total_Current - total_N
        val2 = total_Current_Sqr - total_Sqr_N 

        val2 = val2 // val1

        repeat = (val1 + val2) // 2
        missing = val2 - repeat

        return [repeat, missing]






S = Solution()

arr = [6, 5, 8, 7, 1, 4, 1, 3, 2]
print(S.findTwoElement_Brute(arr))
print(S.findTwoElement_Better(arr))
print(S.findTwoElement_Optimal(arr))