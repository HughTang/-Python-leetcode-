#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    # 解题思路：递归DFS
    # 我们想知道网格中有多少个连通体。
    # 如果我们在一个土地上，以4个方向探索与之相连的每一个土地（以及与这些土地相连的土地），为了确保每个土地访问不超过一次，我们每次经过一块土地时，
    # 将这块土地的值置为0。这样我们就不会多次访问同一土地。如此一来，访问不同岛屿的数量就等于调用DFS函数的次数。
    def numIslands(self, grid: List[List[str]]) -> int:
        # 处理两种不合题意的特殊情况
        if not grid or len(grid) == 0:
            return 0
        # 获取矩阵的行和列的长度
        self.m, self.n = len(grid), len(grid[0])
        # 定义四个方法长度
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # 初始化结果为0
        ans = 0
        # 按照下标遍历矩阵
        for i in range(self.m):
            for j in range(self.n):
                # 如果当前元素为1，才进行DFS
                if grid[i][j] == "1":
                    # 找到一个岛屿，将其所有土地都置为0
                    self.dfs(grid,i,j)
                    # 岛屿数量+1
                    ans += 1
        # 返回最终结果
        return ans

    def dfs(self, grid: List[List[str]], row: int, col: int) -> int:
        # 递归出口：当前下标越界或当前元素不为1（为0），那么直接返回0
        if row < 0 or row >= self.m or col < 0 or col >= self.n or grid[row][col] == "0":
            return 0
        # 为了防止重复遍历同一个节点，所以将遍历过的节点置为0
        # 需要注意的是，python传递的参数都是变量的引用，因此在这个改变grid中的值，maxAreaOfIsland中grid中的值也会改变
        grid[row][col] = "0"
        # 针对四个方向进行DFS递归遍历
        for i,j in self.directions:
            self.dfs(grid,i+row,j+col)
# @lc code=end

