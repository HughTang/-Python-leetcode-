#
# @lc app=leetcode.cn lang=python3
#
# 剑指 Offer 50. 第一个只出现一次的字符
#
# 题目描述：在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
class Solution:
    # 方法一：哈希表
    def firstUniqChar(self, s: str) -> str:
        dic = dict()
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return ' '
    
    # 方法二：数组
    def firstUniqChar(self, s: str) -> str:
        ls = [0] * 26
        for c in s:
            ls[ord(c)-ord('a')] += 1  
        for c in s:
            if ls[ord(c)-ord('a')] == 1:
                return c
        return ' '