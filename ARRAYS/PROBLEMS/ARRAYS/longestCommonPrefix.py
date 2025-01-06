from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        matchWord = strs[0]

        for wordsInd in range(1, len(strs)):

            if len(strs[wordsInd]) == 0:
                return ""
            else:
                for charInd in range(0, min(len(matchWord), len(strs[wordsInd]))):
                    if strs[wordsInd][charInd] != matchWord[charInd]:
                        matchWord = matchWord[0 : charInd]
                        break
                    elif charInd == min(len(matchWord), len(strs[wordsInd])) - 1:
                        matchWord = matchWord[0 : charInd + 1]
                        
        return matchWord
    


S = Solution()
# strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
print(S.longestCommonPrefix(strs))