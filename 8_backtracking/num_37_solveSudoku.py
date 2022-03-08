class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_vaild(row, col, val, board):
            for i in board[row]:
                if i == val:
                    return False
            for row_list in board:
                if row_list[col] == val:
                    return False
            # 判断同一九宫格是否有冲突
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == str(val):
                        return False
            return True

        def backtracking(board):
            # 若有解，返回True；若无解，返回False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != ".":
                        continue
                    for k in range(1, 10):
                        if is_vaild(i, j, str(k),board):
                            board[i][j] = str(k)
                            if backtracking(board):
                                return True
                            board[i][j] = '.'
                    return False
            return True

        backtracking(board)


s = Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])