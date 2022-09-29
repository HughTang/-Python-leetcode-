#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
# 注：该题不允许将数字转换为字符串处理，但我们仍然给出使用字符串与不适用字符串的两种解法。
class Solution(object):
    # 解法一：使用字符串
    # def isPalindrome(self, x):
    #     return str(x)[::-1] == str(x)


    # 解法二：不适用字符串（重要），为了防止整数溢出的情况，这里使用反转数字的一半的方法
    def isPalindrome(self, x):
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0
        # 只有 0 满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversedNumber = 0
        while x > reversedNumber:
            reversedNumber = reversedNumber * 10 + x % 10
            x = x // 10
        
        # 当数字长度为奇数时，我们可以通过 revertedNumber // 10 去除处于中位的数字。
        # 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == reversedNumber or x == reversedNumber // 10
# @lc code=end

