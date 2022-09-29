#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    # 使用栈：可以实现删除两个相邻且相同字母的操作，
    # 但需要注意的是，该题目不是完全去重，而是去除相邻重复项。
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
# @lc code=end

