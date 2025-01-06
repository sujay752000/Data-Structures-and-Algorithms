from collections import defaultdict

class Solution:
    def solve_Brute(self, A, B):
        count = 0

        for i in range(0, len(A)):
            prefix_XOR = 0
            for j in range(i, len(A)):
                prefix_XOR ^= A[j]

                if prefix_XOR == B:
                    print(A[i : j + 1])
                    count += 1

        print(count)


    def solve_Optimal(self, A, B):
        hashMap = defaultdict(int)
        hashMap[0] = 1
        prefix_XOR = 0
        count = 0
        for num in A:
            prefix_XOR ^= num
            
            target = B ^ prefix_XOR
            count += hashMap[target]
            
            hashMap[prefix_XOR] += 1
            
        return count
            

S = Solution()
A = [6, 3, 1, 5, 1, 4, 2, 2]
B = 6
print(S.solve_Optimal(A, B))
S.solve_Brute(A, B)