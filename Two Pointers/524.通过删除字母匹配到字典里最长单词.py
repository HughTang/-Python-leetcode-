#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    # 返回符合条件的字符串
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 定义一个longestWord的字符串类型变量进行子串的预保存
        longestWord = ""
        for word in dictionary:
            l1, l2 = len(longestWord), len(word)
            # 将符合要求的子串遴选，返回最长或长度相等但最靠前的子串。
            if l1 > l2 or (l1 == l2 and word > longestWord):
                continue
            if self.subStr(s, word):
                longestWord = word
        return longestWord

    # 判断字典串中的字符串是否为指定字符串的子串
    def subStr(self, s: str, target: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target) 


# 2021-09-14自行解题代码如下，findLongestWord函数没有之前的方法巧妙，但是易于理解，前后两种方法的时间复杂度和空间复杂度差不多
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ''
        maxlen = 0
        for x in dictionary:
            if self.subString(s,x):
                if maxlen < len(x):
                    maxlen = len(x)
                    ans = x
                if maxlen == len(x) and x < ans:
                    ans = x
        return ans
    
    def subString(self, s: str, x: str) -> bool:
        p1 = p2 = 0
        while p1 < len(s) and p2 < len(x):
            if s[p1] == x[p2]:
                p2 += 1
            p1 += 1
        return p2 == len(x)
# @lc code=end

