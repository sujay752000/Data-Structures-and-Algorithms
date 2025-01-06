class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        CapitalCase = [0] * 26
        LowerCase = [0] * 26

        for char in stones:
            if char.islower():
                LowerCase[ord(char) - ord("a")] += 1
            else:
                CapitalCase[ord(char) - ord("A")] += 1


        res = 0

        for char in jewels:
            if char.islower():
                res += LowerCase[ord(char) - ord("a")]
            else:
                res += CapitalCase[ord(char) - ord("A")]

        return res



S = Solution()
jewels = "aA"; stones = "aAAbbbb"
print(S.numJewelsInStones(jewels, stones))