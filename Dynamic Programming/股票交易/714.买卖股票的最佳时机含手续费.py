#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    # 方法一：两种状态DP（空间未优化）
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        # have: 手上持有股票的最大收益，第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
        # no: 手上不持有股票的最大收益
        have = [-prices[0]] + [0] * (n - 1)
        no = [0] * n
        for i in range(1,n):
            # 第i天结束后持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则当前股票是从第i-1天就已经持有的；
            # （2）第i天进行买入，那么第i−1天就不能持有股票，然后减去买股票的负收益prices[i]。
            have[i] = max(have[i-1], no[i-1] - prices[i])
            # 第i天结束后不持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则第i-1天就不持有股票；
            # （2）第i天卖出股票，则第i-1天必须持有股票，然后加上卖出股票的正收益prices[i]，减去手续费fee
            no[i] = max(no[i-1], have[i-1] + prices[i] - fee)
        return no[-1]
    
    # 方法二：两种状态DP（空间优化）
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        # have: 手上持有股票的最大收益，第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
        # no: 手上不持有股票的最大收益
        have, no = -prices[0], 0
        for i in range(1,n):
            new_have = max(have, no - prices[i])
            new_no = max(no, have + prices[i] - fee)
            have, no = new_have, new_no
        return no
# @lc code=end

