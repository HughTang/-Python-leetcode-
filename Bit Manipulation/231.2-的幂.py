#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 方法一：将n转化为二进制，然后判断其中1的个数是否为1
        # return n > 0 and bin(n).count('1') == 1
        # return n > 0 and format(n,'b').count('1') == 1

        # 方法二：利用n & (n - 1)去除n的位级表示中最低的那一位1，判断剩余的位数是否都为0
        return n > 0 and n & (n - 1) == 0
        
        # 方法三：利用n & (-n)获取n的位级表示中最低的那一位1，判断其是否与n相等
        # return n > 0 and n & (-n) == n
# @lc code=end

