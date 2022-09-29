# 母牛生产
# 程序员代码面试指南-P181

# 题目描述
# 假设农场种中成熟的母牛每年都会生 1 头小母牛，并且永远都不会死。第一年有 1 只小母牛，从第二年开始，母牛开始生小母牛。
# 每只小母牛 3 年后成熟又可以生小母牛。给定整数 N，求N年后牛的数量。

# 思路分析
# 第 i 年母牛的数量为 dp[i] 等于 上一年的母牛数量 dp[i - 1] 加上 新出生的母牛数量dp[i - 3]，即3年前的母牛数量，3年前的母牛现在都可以生一头小母牛。

# 状态转移方程
# dp[i] = dp[i - 1] + dp[i - 3]

# @lc code=start
class Solution:
    # 空间复杂度为O(N)
    def cowNums(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * n
        # dp[0]表示第一年的母牛数量，以此类推
        dp[0], dp[1], dp[2] = 1, 2, 3
        for i in range(3,n):
            dp[i] = dp[i - 1] + dp[i - 3]
        return dp[-1]
# @lc code=end