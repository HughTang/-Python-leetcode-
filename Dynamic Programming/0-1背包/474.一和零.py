#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    # 多维费用的0-1背包问题，有两个背包大小，即0的数量和1的数量
    # dp[i][j]表示容量为i个0和j个1的背包所能承载的子集数量
    # 
    # 状态转移方程：
    # (1)当i >= zeros且j >= ones
    #   dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
    # (2)当i < zeros或j < ones
    #   dp[i][j] = dp[i][j]
    # 因此，为了简化步骤，可以将(2)的情况省略，所以需要对二维数组dp的进行倒序嵌套遍历，其中i需要从m遍历到zero，j需要从n遍历到ones
    # 
    # 复杂度分析：
    # 时间复杂度：O(lmn+L)，其中l是数组strs的长度，m和n分别是0和1的容量，L是数组strs中的所有字符串的长度之和。
    # 空间复杂度：O(mn)，其中m和n分别是0和1的容量
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros =s.count('0') 
            ones = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[-1][-1]
# @lc code=end

