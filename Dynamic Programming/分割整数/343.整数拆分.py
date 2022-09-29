#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    # 动态规划说明
    # 本题与剑指offer第14题剪绳子是同一个题目，由于在递推公式中存在实际下标的值（即j和i-j），因此本题中dp的下标必须与实际的整数大小（绳子长度） 一致，
    # 所以在初始化和for循环时都应注意下标的范围是从0到n的，且需要与 斐波那契数列 题组中的dp[0]代表数值为1的情况区分开来。
    #
    # 算法思想：
    # dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积，初始dp[0]和dp[1]都无意义，因此初始化为0。
    # 对长度为i的绳子, 在j处的切割后, 接下来有两种选择:
    # （1）继续切(i - j)长度的绳子, 则ans = j * dp[i - j]
    # （2）不切了, 则ans = j * (i - j)
    # 由于切j和切i-j的效果是一样的，所以嵌套循环中的条件设置为从1到i//2+1即可
    # 
    # 复杂度分析
    # 时间复杂度为O(N²)，空间复杂度为O(N)
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i//2 + 1):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
    
    # 贪心算法
    # 时间复杂度和空间复杂度都是O(1)
    def integerBreak(self, n: int) -> int:
        if n <= 3: 
            return n - 1
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        # 当n<=4时，不再做分割便是最优的结果
        return ans * n
# @lc code=end