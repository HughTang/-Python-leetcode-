#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # 该题的状态转移方程为斐波那契数列的方程

    # 方法一：递归
    # 根据状态转移方程直接递归，但该方法会超时
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    # 方法二：顺推
    # 借助一个列表，存储f(x)的每个值，空间复杂度为O(N)
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0] * n
        # 这里的dp[0]和dp[1]分别表示爬1层和爬2层楼梯的情况
        dp[0], dp[1] = 1, 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
    # 方法三：顺推
    # 使用两个变量，记录每轮循环中f(n-1)和f(n-2)的值，空间复杂度为O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        # a记录f(n-2)，b记录f(n-1)
        a, b = 1, 2
        for _ in range(2,n):
            # 借助中间变量
            # tmp = b
            # b = a + b
            # a = tmp

            # 不借助中间变量
            b, a = a + b, b
        return b
# @lc code=end

