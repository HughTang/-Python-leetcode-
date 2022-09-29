# 在第20题的题目要求基础上，括号有增加了优先级，需要保证优先级高的不能被优先级低的嵌套
class Solution:
    def isPriorityValid(self, s: str) -> bool:
        dic = {'}': '{', ']': '[', ')': '('}
        # 定义优先级字典
        priority = {'{': 3, '[': 2, '(': 1}
        stack = list()
        for c in s:
            if stack and c in dic:
                if dic[c] != stack.pop():
                    return False
        # 在第20题的基础上添加/修改得到以下代码
        # --------diff-------------
            elif stack and priority[stack[-1]] < priority[c]:
                return False
        # --------diff-------------
            else:
                stack.append(c)
        return not stack