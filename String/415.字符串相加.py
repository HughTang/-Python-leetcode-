#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        index_num1 = len(num1) - 1
        index_num2 = len(num2) - 1
        carry = 0
        s = str()
        while index_num1 >= 0 or index_num2 >=0 or carry > 0:
            a = int(num1[index_num1]) if index_num1 >= 0 else 0
            b = int(num2[index_num2]) if index_num2 >= 0 else 0
            index_num1 -= 1
            index_num2 -= 1
            num = a + b + carry
            carry = num // 10
            num %= 10
            s += str(num)
        return s[::-1]
# @lc code=end

