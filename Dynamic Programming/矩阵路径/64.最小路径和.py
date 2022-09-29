#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start

# 动态规划在二维数组（矩阵）中的应用
# 
# 状态定义：
# 设dp为大小m×n矩阵，其中dp[i][j]的值代表直到走到(i,j)的最小路径和。

# 转移方程：
# 题目要求，只能向右或向下走，换句话说，当前单元格(i,j)只能从左方单元格(i−1,j)或上方单元格(i,j−1)走到，因此只需要考虑矩阵左边界和上边界。
# 走到当前单元格(i,j)的最小路径和=“从左方单元格(i-1,j)与从上方单元格(i,j-1)走来的两个最小路径和中较小的”+当前单元格值grid[i][j]。具体分为以下4种情况：
# （1）当上边和左边都不是矩阵边界时，即i≠0，j≠0时，dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]；
# （2）当只有左边是矩阵边界时，即i≠0，j=0时，dp[i][j] = dp[i-1][j] + grid[i][j]；
# （3）当只有上边是矩阵边界时，即i=0，j≠0时，dp[i][j] = dp[i][j-1] + grid[i][j]；
# （4）当上边和左边都是矩阵边界时，即i=0，j=0时，dp[i][j] = grid[i][j]。

# 返回值
# 返回dp矩阵右下角值，即走到终点的最小路径和。

# 优化
# 其实我们完全不需要建立dp矩阵浪费额外空间，直接遍历grid[i][j]修改即可。这是因为：grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]；
# 原 grid 矩阵元素中被覆盖为 dp 元素后（都处于当前遍历点的左上方），不会再被使用到。

# 复杂度分析：
# 时间复杂度为O(M×N)： 遍历整个grid矩阵元素。
# 空间复杂度为O(1)： 直接修改原矩阵，不使用额外空间。

class Solution:
    # 优化前：使用dp数组，空间复杂度为O(M×N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        # 初始化二维数组，这里的for循环不能改为*号，因为python内存机制的问题，用*号只是把对象引用多次，并没有创建新的对象，会对后面的赋值操作产生影响
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                # 当上边和左边都是矩阵边界时
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                # 当只有上边是矩阵边界时
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                # 当只有左边是矩阵边界时
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                # 当上边和左边都不是矩阵边界时
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
    
    # 优化后：直接在原数组上操作，空间复杂度为O(1)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(columns):
                # 当上边和左边都是矩阵边界时
                if i == j == 0:
                    continue
                # 当只有上边是矩阵边界时
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                # 当只有左边是矩阵边界时
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                # 当上边和左边都不是矩阵边界时
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

