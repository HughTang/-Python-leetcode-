#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
# 解法一：涉及visited中元素的新增和删减，该解法中将dfs函数中的递归结果赋给res，最终返回res，易于理解
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, set()):
                    return True
        return False
    
    def dfs(self, board, word, row, col, visited):
        if not word:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0] or (row,col) in visited:
            return False
        visited.add((row,col))
        res = self.dfs(board, word[1:], row, col+1, visited) or self.dfs(board, word[1:], row, col-1, visited) or self.dfs(board, word[1:], row+1, col, visited) or self.dfs(board, word[1:], row-1, col, visited)
        visited.remove((row,col))
        return res    

                
# 解法二
class Solution: 
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 处理特殊情况
        if not word:
            return True
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        # 初始化行列长和方向集合
        self.m, self.n = len(board), len(board[0])
        self.directions = {(-1,0), (1,0), (0,-1), (0,1)}

        # 以board中每个节点为起点，对其进行DFS递归判断
        for i in range(self.m):
            for j in range(self.n):
                # 初始化visited数组为全False，防止DFS过程中二次利用已遍历节点元素
                visited = [[False] * self.n for _ in range(self.m)]
                # DFS递归回溯，传入board，word，坐标和visited数组
                if self.dfs(board, word, i, j, visited):
                    # 找到一条符合条件的路径，就返回True
                    return True
        # 没有符合条件的路径，返回False
        return False
    
    # DFS递归回溯
    def dfs(self, board: List[List[str]], word: str, row: int, col: int, visited: List[List[bool]]) -> bool:
        # 如果word为空字符串，则说明找到了一条合适的路径，返回True
        if not word:
            return True
        # 如果坐标超出范围or被访问过or当前元素与word的第一个元素不相同，则返回False
        if row < 0 or row >= self.m or col < 0 or col >= self.n or visited[row][col] == True or board[row][col] != word[0]:
            return False
        
        # 当前元素与word的第一个元素相同，那么将其标记为已访问
        visited[row][col] = True

        # 根据四个方向进行DFS遍历
        for i,j in self.directions:
            if self.dfs(board, word[1:], row+i, col+j, visited):
                return True

        # 如果程序运行到此，说明本轮访问的board[row][col]不是合适的路径，则将visited[row][col]重新恢复为未访问状态，以保证以后可以被其他路径访问到
        visited[row][col] = False

        # 未找到目标路径，返回False
        return False
# @lc code=end

