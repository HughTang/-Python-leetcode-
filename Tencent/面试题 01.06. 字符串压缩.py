# 题目描述
# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
# 比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
class Solution:
    # 方法一：常规思路
    def compressString(self, S: str) -> str:
        if not S:
            return S
        num = 0
        ch = S[0]
        ans = ''
        for c in S:
            if c == ch:
                num += 1
            else:
                ans += ch + str(num)
                ch, num = c, 1
        ans += ch + str(num)
        return ans if len(ans) < len(S) else S

    # 方法二：栈
    def compressString(self, S: str) -> str:
        stack = list()
        for c in S:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
        ans = ''
        for x,y in stack:
            ans += x + str(y) 
        return ans if len(ans) < len(S) else S