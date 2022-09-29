#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
class Solution:
    # 本题主要问题是判断两个字符串是否含相同字符，由于字符串只含有
    # 小写字符，总共 26 位，因此可以用一个 32 位的整数来存储每个
    # 字符是否出现过。
    def maxProduct(self, words: List[str]) -> int:
        # n为所有的字符串个数
        n = len(words)
        # 初始化整数数组，用于存储每个字符串中出现的字符用二进制表示后得到的整数
        nums = [0] * n
        # 遍历每个字符串
        for i, word in enumerate(words):
            # 遍历当前字符串中的字符
            for c in word:
                # 存储每个字符与'a'的差值对1左移后的或运算结果
                nums[i] |= 1 << int(ord(c) - ord('a'))
        # 将结果变量初始化为0
        ans = 0
        # 利用一个嵌套下标循环来获取最终结果
        for i in range(n):
            for j in range(i+1,n):
                # 如果两个字符串所表示的整数没有相同的'1'位，则说明对应的两个字符串没有相同字符，可以计算长度的积
                if nums[i] & nums[j] == 0:
                    # 利用max函数来获取满足条件的最大结果
                    ans = max(ans, len(words[i] * len(words[j])))
        # 返回最终结果
        return ans 
# @lc code=end

