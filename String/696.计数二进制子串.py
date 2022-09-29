#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
# 问题本质：统计二进制字符串中连续1和连续0数量相同的子字符串个数
# 1、计算当前这个与前面字符是否相同，并记录个数，curLen
# 2、when当前的字符与前面的字符不相同时，将前面字符的个数保存,preLen
# 3、当preLen>=curLen时，说明存在01和0011这两种情况中的一种，所以个数count=1

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
         # 记录当前重复字符串的个数
         curLen = 1
         preLen = 0
         # 记录子串的个数
         count = 0

         for i in range(1,len(s)):
             if s[i] == s[i-1]:
                curLen += 1
             else:
                preLen = curLen
                curLen = 1
             if preLen >= curLen: # preLen>=curLen很重要，如果是>，则存在01或者10的情况，若=时，就存在0011或1100这种情况。仔细读一下代码即可
                count += 1
         
         return count
# @lc code=end

