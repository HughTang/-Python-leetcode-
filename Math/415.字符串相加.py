#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ''
        while p1 >= 0 or p2 >= 0 or carry != 0:
            a = int(num1[p1]) if p1 >= 0 else 0
            b = int(num2[p2]) if p2 >= 0 else 0
            num = a + b + carry
            carry = num // 10
            ans = str(num % 10) + ans
            p1 -= 1
            p2 -= 1
        return ans
# @lc code=end

