from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hashBlocks = defaultdict(set)   # block (row // 3, col // 3) : {val}
        hashRows = defaultdict(set)     # row : {val}
        hashCols = defaultdict(set)     # col : {val}

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue
                val = board[row][col]
                if val in hashRows[row] or val in hashCols[col] or val in hashBlocks[(row // 3, col // 3)]:
                    return False
                hashRows[row].add(val)                      # adding val to respective row, i,e row : {val}
                hashCols[col].add(val)                      # adding val to respective col, i,e col : {val}
                hashBlocks[(row // 3, col // 3)].add(val)   # adding val to respective block, i,e (row // 3, col // 3) : {val}
        return True




S = Solution()
board = [[".","2",".",  ".",".",".",  ".",".","."],
         [".",".",".",  ".",".",".",  "5",".","1"],
         [".",".",".",  ".",".",".",  "8","2","3"],

         ["4",".","9",  ".",".",".",  ".",".","."],
         [".",".",".",  ".",".",".",  ".",".","."],
         [".",".","2",  ".",".",".",  ".",".","."],

         ["7",".","6",  ".",".",".",  ".",".","."],
         ["9",".",".",  ".",".","4",  ".",".","."],
         [".",".",".",  ".",".",".",  ".",".","."]]

print(S.isValidSudoku(board))