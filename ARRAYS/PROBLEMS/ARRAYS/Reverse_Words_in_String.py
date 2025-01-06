class Solution:
    def reverseWords(self, s: str) -> str:
        res_str = ""
        space = 0
        ind = len(s) - 1

        while ind >= 0:
            word = ""                       # stores each word
            while ind >= 0 and s[ind] != " ":
                word = s[ind] + word        # reverse each word
                ind -= 1
            
            while ind >= 0 and s[ind] == " ":
                space += 1                  # count the spaces
                ind -= 1

            if word:
                if len(res_str) + len(word) + space == len(s):
                    res_str += word
                    break
                space -= 1                  # decrementing space by 1 .. because we are adding 1 space between two words
                res_str += word + " "

        return res_str
            




S = Solution()
s = "  hello world  sujay    prasad   "
print(S.reverseWords(s))