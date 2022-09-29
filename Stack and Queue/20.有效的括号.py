#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            # 栈不为空且s中元素在字典中
            if stack and c in dic: 
                # 判断栈顶元素与dic[c]是否匹配，不匹配时直接返回False
                if dic[c] != stack.pop():
                    return False
            # 栈空或者c为左括号时进栈
            else: 
                stack.append(c)
        return not stack
# @lc code=end

