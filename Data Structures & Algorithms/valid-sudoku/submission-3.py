class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                # if( board[r][c] in rows[r][c] or board[r][c] in col[r][c] or 
                #     board[r][c] in squares[(r // 3), c // 3]): set不是二维数组，而是行或者列的集合
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True




        #好处是检查每一个的数字时候就能查看每行每一列每一组是否重复
        # 用三个哈希几何结构记录已经出现过的数字
        # rows[r] cols[c] boxes[(r // 3, c // 3)]记录对应3*3 box的数字
        # 遍历每个格子，如果是.就跳过，
        # 否则检查这个数字是否存在已经对应的row、col或者box中
        # 存在返回False
        # 否则就加入这三个集合