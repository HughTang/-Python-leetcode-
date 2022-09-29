#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    # 此题可以转化为求「1143.最长公共子序列」的问题，
    # 除了返回值需要变化之外，其他部分完全一样
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # 两个字符串的长度减去两个公共子序列的长度，即为最终的删除操作步数
        return m + n - 2 * dp[-1][-1]
# @lc code=end

