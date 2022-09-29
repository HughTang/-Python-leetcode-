#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    # 完全背包的动态规划问题
    # 定义状态：
    # dp[i]表示现有硬币可以凑成总金额为i的硬币组合方案数
    # （1）边界值：由于总金额为0时，不需要用到coins中的任何硬币，
    # 所以只有不取硬币的一种方案，因此dp[0] = 1
    # （2）初始化：本题所求的是所有的方案数，最少只能为0，因此dp =[1] + [0] * amount
    # 
    # 状态转移方程：
    # 该问题为不用方案的总数问题，因此方程为dp[i] += dp[i-coin]
    #
    # 完全背包问题说明：
    # 因为外层循环是遍历数组coins的值，内层循环是遍历不同的金额之和，
    # 在计算dp[i]的值时，可以确保金额之和等于i的硬币面额的顺序，由于
    # 顺序确定，因此不会重复计算不同的排列。
    # 
    # 复杂度分析：
    # 时间复杂度：O(amount*n)，其中amount是总金额，n是数组coins的长度。需要使用数组coins中的每个元素遍历并更新数组dp中的每个元素的值。
    # 空间复杂度：O(amount)，其中amount是总金额。需要创建长度为amount+1的数组dp。
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[1] + [0] * amount
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]
# @lc code=end

