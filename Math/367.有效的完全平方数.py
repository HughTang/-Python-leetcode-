#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    # 方法一：使用python中的**运算符
    def isPerfectSquare(self, num: int) -> bool:
        return num ** 0.5 % 1 == 0 

    # 方法二：完全平方数之间的间隔是等差数列：3,5,7,9....
    def isPerfectSquare(self, num: int) -> bool:
        subNum = 1
        while num > 0:
            num -= subNum
            subNum += 2
        return num == 0
# @lc code=end

