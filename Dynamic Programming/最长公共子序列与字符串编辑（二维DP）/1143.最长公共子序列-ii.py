# 题目要求：
# 给定两个字符串str1和str2，输出两个字符串的最长公共子序列。如果最长公共子序列为空，则返回"-1"。
# 目前给出的数据，仅仅会存在一个最长的公共子序列。

# 题目网址：https://www.nowcoder.com/questionTerminal/6d29638c85bb4ffd80c020fe244baf11

class Solution():
    def LCS(self , s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        # 由于最后的return中添加了对dp[-1][-1]的判断，所以这里的m和n的为0判断可以省略
        # if m == 0 or n == 0:
        #     return '-1'
        dp = [[''] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + s1[i-1]
                else:
                    dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
        return dp[-1][-1] if dp[-1][-1] != '' else -1