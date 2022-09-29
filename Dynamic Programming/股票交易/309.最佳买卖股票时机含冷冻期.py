#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    # 股票交易专题是 多状态的动态规划问题
    # 方法一：三种状态DP（空间未优化）
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # have: 手上持有股票的最大收益,第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
        # no: 手上不持有股票，并且不在冷冻期中的累计最大收益
        # cold: 手上不持有股票，并且处于冷冻期中的累计最大收益
        have = [-prices[0]] + [0] * (n - 1)
        no = [0] * n
        cold = [0] * n
        for i in range(1, n):
            # 第i天结束之后持有股票，其等于以下两种情况的最大值：
            # （1）第i天无任何操作，则当前股票是从第i-1天就已经持有的；
            # （2）第i天进行买入，那么第i−1天就不能持有股票并且不处于冷冻期中，然后减去买股票的负收益prices[i]。
            have[i] = max(have[i-1], no[i-1] - prices[i])
            
            # 第i天结束之后不持有任何股票并且不处于冷冻期，说明当天没有进行任何操作
            # 其等于以下两种情况的最大值：
            # （1）第i-1天不持有股票且不在冷冻期中
            # （2）第i-1天不持有股票且在冷冻期中
            no[i] = max(no[i-1], cold[i-1])
            
            # 第i天结束之后不持有任何股票且处于冷冻期，说明在第i−1天时
            # 必须持有一支股票，对应的状态为加上卖出股票的正收益prices[i]。
            cold[i] = have[i-1] + prices[i]
        return max(no[-1], cold[-1])
    
    # 方法二：三种状态DP（空间优化）
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # have: 手上持有股票的最大收益,第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
        # no: 手上不持有股票，并且不在冷冻期中的累计最大收益
        # cold: 手上不持有股票，并且处于冷冻期中的累计最大收益
        have, no, cold = -prices[0], 0, 0
        for i in range(1, n):
            new_have = max(have, no - prices[i])
            new_no = max(no, cold)
            new_cold = have + prices[i]
            have, no, cold = new_have, new_no, new_cold
        return max(no, cold)
# @lc code=end

