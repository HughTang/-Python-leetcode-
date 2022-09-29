#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    # 解题思路
    # 采取逆向思维求解，从四个边界开始遍历，使得水往低处流，获取两个大洋的水（四个边界）反着流所能达到的点。
    # （1）找出所有从太平洋出发的水所能达到的点，存储在reach_P二维数组中
    # （2）找出所有从大西洋出发的水所能达到的点，存储在reach_A二维数组中
    # （3）reach_P和reach_A中重合的点即为符合条件的点
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 处理特殊情况
        if not heights:
            return []
        
        # 初始化行列长度和方向集合
        self.m, self.n = len(heights), len(heights[0])
        self.directions = {(-1,0), (0,-1),(1,0), (0,1)}
        
        # 定义结果列表ans
        ans = list()
        # 定义可达太平洋二维标识数组reach_P
        reach_P = [[False] * self.n for _ in range(self.m)]
        # 定义可达大西洋二维标识数组reach_A 
        reach_A = [[False] * self.n for _ in range(self.m)]
        
        # 对四个边界进行DFS，标识太平洋和大西洋的可达节点，DFS结束后会存储在reach_P与reach_A中
        for i in range(self.m):
            self.dfs(heights, i, 0, reach_P)
            self.dfs(heights, i, self.n-1, reach_A)
        for j in range(self.n):
            self.dfs(heights, 0, j, reach_P)
            self.dfs(heights, self.m-1, j, reach_A)

        # 将reach_P与reach_A中重合的元素下标加入结果列表中
        for i in range(self.m):
            for j in range(self.n):
                if reach_P[i][j] and reach_A[i][j]:
                    ans.append([i,j])
        # 返回结果列表
        return ans
    
    # 这里传入的reach二维数组担任了传统visited集合的作用
    def dfs(self, heights: List[List[int]], row: int, col: int, reach: List[List[bool]]):
        # 递归出口：当前元素已被访问过
        if reach[row][col]:
            return
        # 当前元素未被访问过，需要将其加入reach中，改变其状态
        reach[row][col] = True
        # 从四个方向进行DFS
        for i,j in self.directions:
            x, y = row + i, col + j
            # 需要特别注意的是，越界判断之所以放在循环内部而不放在递归出口（DFS函数开始位置）的原因：
            # 相邻位置的元素（heights[row+i][col+j]）与初始位置的元素(heights[row][col])需要进行大小判断。
            # 因此大小比较和越界判断必须放在同一位置，再进行递归。
            if 0 <= x < self.m and 0 <= y < self.n and heights[x][y] >= heights[row][col]:
                self.dfs(heights, x, y, reach) 
# @lc code=end