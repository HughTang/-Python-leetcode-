#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    # 双指针法的应用
    def validPalindrome(self, s: str) -> bool:
        # 定义lambda匿名函数并命名为isPalindrome，用于判断一个给定的字符串是否是回文串
        isPalindrome = lambda s: s == s[::-1]
        # 提前判断s本身是否为回文串
        if isPalindrome(s):
            return True
        # 左指针初始化为下标0
        left = 0
        # 右指针初始化为下标len(s) - 1
        right = len(s) - 1
        # 循环体结构保证循环过程中left始终小于right
        while left < right:
            # 如果left和right指向的字符相同，则left右移，right左移，并跳出本次循环，直接进行下次循环
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            # 当出现left与right指向字符不相同时，直接对针对删除左字符和删除右字符两种情况进行回文串判断
            return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
# @lc code=end

