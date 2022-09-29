#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    # 本题给定的矩阵中有三种元素：
    # （1）字母X
    # （2）被字母X包围的字母O
    # （3）没有被字母X包围的字母O
    # 本题要求将所有被字母X包围的字母O都变为字母X，但很难判断哪些O是被包围的，哪些O不是被包围的。
    # 注意到题目解释中提到：任何边界上的 O 都不会被填充为 X。 我们可以想到，所有的不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上，具体地说：
    # （1）对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母O，将其替换为T
    # （2）最后我们遍历这个矩阵，对于每一个字母：
    # ①如果该字母被标记为T，则该字母为没有被字母X包围的字母O，我们将其还原为字母；
    # ②如果该字母没有被标记，则该字母为被字母X包围的字母O，我们将其修改为字母X。
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 初始化行列长度和方向列表
        self.m, self.n = len(board), len(board[0])
        self.directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # 将边界上的'O'及相连的'O'全部替换为'T'
        for i in range(self.m):
            self.dfs(board,i,0)
            self.dfs(board,i,self.n-1)
        for j in range(self.n):
            self.dfs(board,0,j)
            self.dfs(board,self.m-1,j)
        
        # 遍历矩阵的每个元素，将为标记的'O'替换为'X'，将标记过的'T'替换为'O'
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
    
    # DFS遍历：将边界上的'O'及相连的'O'全部替换为'T'
    def dfs(self, board: List[List[str]], x: int, y: int):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or board[x][y] != 'O':
            return 0
        board[x][y] = 'T'
        for i,j in self.directions:
            self.dfs(board, x+i, y+j)


# 解法二：借助visited集合记录不需要替换的所有O的下标
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited)
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1, visited)
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, visited)
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j, visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        # print(visited)

    def dfs(self, board, row, col, visited):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 'X' or (row,col) in visited:
            return 0
        directions = {(0,1), (0,-1), (1,0), (-1,0)}
        visited.add((row,col))
        for x,y in directions:
            self.dfs(board, row+x, col+y, visited)     
# @lc code=end

