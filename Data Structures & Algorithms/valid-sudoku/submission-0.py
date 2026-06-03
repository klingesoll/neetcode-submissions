class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       for row in range(9):
           seen = set()
           for i in range(9):
            if board[row][i] == ".":
               continue
            if board[row][i] in seen:
                return False
            seen.add(board[row][i])


       for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] ==".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
       for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3)  * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
       return True




# 遍历 9x9 棋盘。
# 每看到一个数字，就检查它是否已经在当前行、当前列、当前九宫格里出现过。
# 出现过 => False
# 没出现过 => 记录下来