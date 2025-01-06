class Solution:

    def encode(self, strs: list[str]) -> str:
        res_str = ""

        for word in strs:
            length = len(word)
            res_str += str(length) + "#" + word

        print(res_str)
        return res_str


    def decode(self, s: str) -> list[str]:

        res_lst = []
        ind = 0

        while ind < len(s):
            delimiter_tracker = ind

            while s[delimiter_tracker] != "#":
                delimiter_tracker += 1

            length = int(s[ind : delimiter_tracker])
            word = s[delimiter_tracker + 1 : delimiter_tracker + length + 1]
            res_lst.append(word)
            ind = delimiter_tracker + length + 1

        return res_lst





S = Solution()
lst = ["neet","code","love", "[""]", "you"]
string = S.encode(lst)
print(S.decode(string))