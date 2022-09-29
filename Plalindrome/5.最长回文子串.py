#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 本题与「647.回文子串」的解答思路基本一致，都是使用中心扩展法。
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            tmp = self.extend_substring(s, i, i)
            if len(tmp) > len(ans):
                ans = tmp
            tmp = self.extend_substring(s, i, i+1)
            if len(tmp) > len(ans):
                ans = tmp
        return ans
    
    # 中心扩展回文子串的函数实现
    def extend_substring(self, s: str, start: int, end: int) -> str:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
# @lc code=end

