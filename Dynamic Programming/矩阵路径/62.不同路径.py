#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# 
# 算法思想
# 本题与「64.最小路径和」的算法思想是相同的，参照该题的思想作答即可。

# 状态转移方程
# dp[i][j] += dp[i-1][j] + dp[i][j-1]

# 简化
# 由于该题中机器人只能向右或者向下走，那么需要初始化上边和左边的边界的dp元素全为1

# 复杂度分析：
# 时间复杂度为O(M×N)： 遍历整个矩阵元素。
# 空间复杂度为O(M×N)： 使用与矩阵大小相同的dp二维数组
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                # 依据状态转移方程赋值
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# 变体：可以走奇数步数（1，3，5...）时，求解不同路径
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = list(range(1,max(n,m),2))
        dp = [[0]* n for _ in range(m)]
        dp[0][0] = 1

        # 初始化上左边界
        for i in range(1,m):
            for x in directions:
                if i-x >= 0:
                    dp[i][0] += dp[i-x][0]
        for j in range(1,n):
            for x in directions:
                if j-x >= 0:
                    dp[0][j] += dp[0][j-x]
        # 状态转移
        for i in range(1,m):
            for j in range(1,n):
                for x in directions:
                    if i-x >= 0 and i-x >= 0:
                        dp[i][j] += dp[i-x][j] + dp[i][j-x]
                    elif i-x >= 0:
                        dp[i][j] += dp[i-x][j]
                    elif j-x >= 0:
                        dp[i][j] += dp[i][j-x]
        return dp[-1][-1]
# @lc code=end

