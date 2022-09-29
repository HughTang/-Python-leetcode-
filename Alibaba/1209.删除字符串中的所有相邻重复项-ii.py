#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 栈中的每个列表分别存储字符和相邻频次
        stack = list()
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ''
        for c,i in stack:
            ans += c * i
        return ans
# @lc code=end

