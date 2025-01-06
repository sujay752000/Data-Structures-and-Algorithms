from collections import defaultdict, Counter
class Solution:
    def frequencySort_Optimal(self, s: str) -> str:
        n = len(s)
        counterMap = Counter(s)         # char : count
        hashMap = defaultdict(list)     # count : [char1, char2 ...]

        for element, count in counterMap.items():
            hashMap[count].append(element)

        res = ""
        for count in range(n, 0, -1):   # O(n)
            elements = hashMap[count]
            
            # if elements is not empty .. then for loop works
            for element in elements:    # + O(n)
                res += element * count  # "e" * 4 = "eeee"

        return res



S = Solution()
s = "etesreess"
print(S.frequencySort_Optimal(s))