class Solution:
    def trailingZeroes_Brute(self, n: int) -> int:
        fact = 1
        for i in range(2, n + 1):
            fact *= i

        count = 0
        print(fact)

        while fact % 10 == 0:
            count += 1
            fact //= 10

        return count
    
    def trailingZeroes_Optimal(self, n: int) -> int:
        ans = 0
        i = 5
        while i <= n:
            ans += n // i
            i *= 5
        return ans

    

S = Solution()
n = 15
print(S.trailingZeroes_Brute(n))
print(S.trailingZeroes_Optimal(n))