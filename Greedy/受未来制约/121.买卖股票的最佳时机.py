#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    # 遍历prices列表，记录当前所遍历的最低价格，并且进行如下操作：
    # （1）获取 当前价格price 与 之前所遍历的最低价格min_price 的最小值
    # （2）获取 当前价格price-最低价格min_price 与 之前所遍历的最大利润max_profit 的最大值
    # 最后返回最大利润max_profit即可
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
# @lc code=end

