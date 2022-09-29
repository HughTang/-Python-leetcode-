#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串（拓展）
#

# @lc code=start
# 注：本题要求返回最长字串本身，而不是长度值
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans = ''
        lookup = dict()
        for i,c in enumerate(s):
            if c in lookup and start <= lookup[c]:
                start = lookup[c] + 1
            else:
                if len(ans) < i-start+1:
                    ans = s[start:i+1]
            lookup[c] = i
        return ans
