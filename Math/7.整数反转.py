#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        if s[-1] == '-':
            s = s[-1]+s[:-1]
        if -2**31 <= int(s) <= 2**31-1:
            return int(s)
        else:
            return 0
# @lc code=start