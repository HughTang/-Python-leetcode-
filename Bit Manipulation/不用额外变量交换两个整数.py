#
# @lc app=leetcode.cn id=461 lang=python3
#
# [P317] 程序员代码面试指南：不用额外变量交换两个整数
#

# @lc code=start
class Solution:
    def exchangeInt(self, x: int, y: int):
        x = x ^ y
        y = x ^ y
        x = x ^ y
