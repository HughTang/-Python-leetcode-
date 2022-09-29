#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # have1: 第一次交易过程中手上持有股票的最大收益，第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
        # no: 第一次交易过程中手上不持有股票的最大收益
        # have2: 第二次交易过程中手上持有股票的最大收益，第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]后再卖出，然后再买入prices[0]
        # no: 第二次交易过程中手上不持有股票的最大收益
        have1 = [-prices[0]] + [0] * (n - 1)
        no1 = [0] * n
        have2 = [-prices[0]] + [0] * (n - 1)
        no2 = [0] * n
        for i in range(1,n):
            # 第一次交易过程中第i天结束后持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则当前股票是从第i-1天就已经持有的；
            # （2）第i天进行买入，那么之前就不能持有股票，只需要取当天股票的负收益-prices[i]即可。
            have1[i] = max(have1[i-1], -prices[i])
            # 第一次交易过程中第i天结束后不持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则第i-1天就不持有股票；
            # （2）第i天卖出股票，则第i-1天必须持有股票，然后加上卖出股票的正收益prices[i]即可。
            no1[i] = max(no1[i-1], have1[i-1] + prices[i])
            # 第二次交易过程中第i天结束后持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则当前股票是从第i-1天就已经持有的；
            # （2）第i天进行买入，那么第i−1天必须是第一次交易已经完成后的收益no1[i-1]，然后减去买股票的负收益prices[i]即可。
            have2[i] = max(have2[i-1], no1[i-1] - prices[i])
            # 第二次交易过程中第i天结束后不持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则第i-1天就不持有股票；
            # （2）第i天卖出股票，则第i-1天必须持有股票，然后加上卖出股票的正收益prices[i]即可。
            no2[i] = max(no2[i-1], have2[i-1] + prices[i])
        return no2[-1]

# @lc code=end

