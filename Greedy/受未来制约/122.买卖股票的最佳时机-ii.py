#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # 贪心的角度考虑我们每次选择贡献大于0的区间即能使得答案最大化。
    # 需要说明的是，贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
            # 上述if语句也可以替换为下面的max语句，因为每次选择贡献大于0的区间即能使得答案最大化，可以省略if语句
            # profit += max(0, prices[i] - prices[i-1])
        return profit
# @lc code=end

