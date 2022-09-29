#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List


class Solution:
    # 字符串的单向回溯，本题与「93.复原IP地址」类似，都需要在for循环中判断题意条件后再递归回溯
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s, ans, [])
        return ans
    
    # DFS递归回溯
    def dfs(self, s: str, ans: List[List[str]], path: List[str]):
        # 递归出口
        if not s:
            ans.append(path)
            return
        for i in range(len(s)):
            # 判断回文
            if s[:i+1] == s[:i+1][::-1]:
                self.dfs(s[i+1:], ans, path+[s[:i+1]])
# @lc code=end

