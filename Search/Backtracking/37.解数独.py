#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)
    
    def dfs(self, board: List[List[str]], row: int, col: int):
        # Go to next empty space
        while board[row][col] != '.':
            col += 1
            if col == 9:
                row += 1
                col = 0
            if row == 9:
                return True
        for k in range(1,10):
            if self.check(board, row, col, str(k)):
                board[row][col] = str(k)
                if self.dfs(board, row, col):
                    return True
        board[row][col] = '.'
        return False
    
    def check(self, board: List[List[str]], row: int, col: int, target: str):
        # 检查行
        if any(board[i][col] == target for i in range(9)): return False
        # 检查列
        if any(board[row][j] == target for j in range(9)): return False 
        # 检查3*3子列表
        br, bc = 3*(row//3), 3*(col//3)
        if any(board[i][j] == target for i in range(br,br+3) for j in range(bc,bc+3)): return False
        return True
# @lc code=end

