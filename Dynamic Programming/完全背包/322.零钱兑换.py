#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # 该题在“分割整数”专题中出现过，而其实本题的官方思路的完全背包问题
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp数组为全float('inf')，为了使后面的顺推过程顺利进行，需要初始化dp[0]为0
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        # 判断零钱是否兑换成功，若兑换成功，则返回dp[-1]，若没有兑换方案，则返回-1
        return dp[-1] if dp[-1] != float('inf') else -1
# @lc code=end

