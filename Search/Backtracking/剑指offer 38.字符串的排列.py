'''
Author: HughTang
Date: 2021-12-13 10:49:38
LastEditors: HughTang
LastEditTime: 2021-12-24 15:52:15
Description: Write your description here..
'''
#
# @lc app=剑指offer id=38 lang=python3
#
# [38] 字符串的排列
# 题目描述：输入一个字符串，打印出该字符串中字符的所有排列。你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
class Solution:
    # 思路解析：使用递归的思想，可以将解答过程分为两步：
    # （1）确定第一个位置的字符，就是第一个位置与与后边的所有字符进行交换。
    # （2）对除了第一个位置的后边所有位置的字符进行相同处理，直至剩下一个字符就返回。
    # 
    # 递归思路：
    # （1）递归的出口：只剩一个字符时
    # （2）递归的循环过程：从每个子串的第二个字符开始依次与第一个字符交换，然后继续处理子串，如果有重复的，然后对结果使用set去重即可
    # 
    # 方法一：在递归处理过程中去重
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        ans = set()
        for i in range(len(s)):
            for j in self.permutation(s[0:i] + s[i+1:]):
                ans.add(s[i]+j)
        return list(ans)
    
    # 方法二：在递归结束后对最终的结果去重
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        ans = list()
        for i in range(len(s)):
            for j in self.permutation(s[0:i] + s[i+1:]):
                ans.append(s[i]+j)
        return list(set(ans))

    # 方法三：回溯
    def permutation(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, ans, '')
        # 去重
        return list(set(ans))
    
    def dfs(self, s: str, ans: List[str], path: str):
        if not s:
            ans.append(path)
            return 
        for i in range(len(s)):
            self.dfs(s[:i]+s[i+1:], ans, path+s[i])
# @lc code=start