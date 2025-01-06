class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        rot_0 = True
        rot_90 = True
        rot_180 = True
        rot_270 = True

        for i in range(0, n):
            for j in range(0, n):
                print(mat[i][j], target[i][j], "MAT = 0")
                if mat[i][j] != target[i][j]:
                    rot_0 = False


                print(mat[i][j], target[j][n - i - 1], "MAT = 90")
                if mat[i][j] != target[j][n - i - 1]:
                    rot_90 = False


                print(mat[i][j], target[n - i - 1][n - j - 1], "MAT = 180")
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    rot_180 = False


                print(mat[i][j], target[n - j - 1][i], "MAT = 270")
                if mat[i][j] != target[n - j - 1][i]:
                    rot_270 - False

        print(rot_0, rot_90, rot_180, rot_270)

        return rot_0 or rot_90 or rot_180 or rot_270


mat = [[0, 1], [1, 1]]
target = [[1,0],[0,1]]
S = Solution()
print(S.findRotation(mat, target))
