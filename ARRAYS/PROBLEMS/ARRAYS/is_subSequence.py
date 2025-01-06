class Solution:
    def findChar(self, t, char_start, char_end, starting_ind, ending_ind) -> tuple[int, int]:
        res_start = -1
        res_end = -1

        res_start_temp = -1
        res_end_temp = -1
        start_find = False
        end_find = False

        # O(m / 2)
        while starting_ind <= ending_ind:
            if t[starting_ind] == char_start and start_find == False:
                res_start = starting_ind
                start_find = True
            elif t[starting_ind] == char_end and start_find == True:
                res_end_temp = starting_ind

            if t[ending_ind] == char_end and end_find == False:
                res_end = ending_ind
                end_find = True
            elif t[ending_ind] == char_start and end_find == True:
                res_start_temp = ending_ind


            if start_find == True and end_find == True:
                break

            starting_ind += 1
            ending_ind -= 1

        if start_find == False and res_start_temp != -1:
            res_start = res_start_temp
        
        if end_find == False and res_end_temp != -1:
            res_end = res_end_temp

        return (res_start, res_end)

    def isSubsequence_Brute(self, s: str, t: str) -> bool:
        start = 0
        end = len(s) - 1

        starting_ind = 0
        ending_ind = len(t) - 1

        # O(n / 2)
        while start <= end:
            res = self.findChar(t, s[start], s[end], starting_ind, ending_ind)
            if start == end and res[0] == -1 and res[1] == -1:
                return False
            elif start == end and (res[0] == -1 or res[1] == -1):
                return True

            if res[0] == -1 or res[1] == -1 or (res[0] == res[1] and start != end):
                return False

            starting_ind = res[0] + 1
            ending_ind = res[1] - 1
            start += 1
            end -= 1
        return True

    def isSubsequence_Optimal(self, s: str, t: str) -> bool:
        # TC = O(m)
        # SC = O(1)
        n = len(s)
        m = len(t)

        subSequence_Tracker = 0
        compareStr_Tracker = 0

        while subSequence_Tracker < n and compareStr_Tracker < m:
            if s[subSequence_Tracker] == t[compareStr_Tracker]:
                subSequence_Tracker += 1

            compareStr_Tracker += 1

        return subSequence_Tracker == n



S = Solution()

# s = "bb"
# t = "ahbgdc"

s = "abc"
t = "ahbgdc"

# s = "bcd"
# t = "uuuuubcd"


print(S.isSubsequence_Brute(s, t))
print(S.isSubsequence_Optimal(s, t))
