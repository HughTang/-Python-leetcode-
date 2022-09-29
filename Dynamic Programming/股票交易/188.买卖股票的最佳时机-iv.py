#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    # https://leetcode-cn.com/problems/best-time-to-have-and-no-stock-iv/solution/si-wei-dao-tu-zheng-li-dpshu-zu-gou-jian-e97c/
    # 方法一：二个状态的DP（空间未优化）
    # 在上述的状态转移方程中，确定边界条件是非常重要的步骤。我们可以考虑将所有的have[0][0..k] 以及no[0][0..k]设置为边界。
    # 对于have[0][0..k]，由于只有prices[0]是唯一的股价，因此我们不可能进行过任何交易，那么我们可以将所有的have[0][1..k]设置为一个非常小的值，表示不合法的状态。而对于have[0][0]，它的值为−prices[0]，即「我们在第0天以prices[0]的价格买入股票」是唯一满足手上持有股票的方法。
    # 对于no[0][0..k]，同理我们可以将所有的no[0][1..k]设置为一个非常小的值，表示不合法的状态。而对于no[0][0]，它的值为0，即「我们在第0天不做任何事」是唯一满足手上不持有股票的方法。
    # 在设置完边界之后，我们就可以使用二重循环，在i∈[1,n),j∈[0,k]的范围内进行状态转移。需要注意的是，no[i][j]的状态转移方程中包含have[i−1][j−1]，在j=0时其表示不合法的状态，因此在j=0时，我们无需对no[i][j]进行转移，让其保持值为0即可。
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices:
            return 0
        
        n = len(prices)
        k = min(k, n//2)
        
        have = [[0] * (k+1) for _ in range(n)]
        no = [[0] * (k+1) for _ in range(n)]

        for i in range(1, k+1):
            have[0][i] = no[0][i] = float('-inf')
        
        have[0][0] = -prices[0]
        no[0][0] = 0

        for i in range(1,n):
            have[i][0] = max(have[i-1][0], no[i-1][0] - prices[i])
            for j in range(1,k+1):
                have[i][j] = max(have[i-1][j], no[i-1][j] - prices[i])
                no[i][j] = max(no[i-1][j], have[i-1][j-1] + prices[i])
        return max(no[-1])
    
    # 方法二：二个状态的DP（空间优化）
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices:
            return 0
        
        n = len(prices)
        k = min(k, n//2)
        
        have = [-prices[0]] + [float('-inf')] * k
        no = [0] + [float('-inf')] * k

        for i in range(1,n):
            have[0] = max(have[0], no[0] - prices[i])
            # 由于have和no的值完全依赖于上一个循环状态的值，所以在将二维数组优化为一维数组时，内层循环需要倒序，这与0-1背包问题的空间优化原理是一致的
            for j in range(k,0,-1):
                have[j] = max(have[j], no[j] - prices[i])
                no[j] = max(no[j], have[j-1] + prices[i])
        return max(no)
# @lc code=end

