#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # 方法一：异或操作，将num与相同位数全为1的数进行异或操作即可
        return num ^ (2**(len(bin(num))-2)-1)

        # 方法二：数学计算，num和补数相加，就是满数位1的二进制数，即2**n-1 == num + complement
        return 2**(len(bin(num))-2)-num-1
# @lc code=end

