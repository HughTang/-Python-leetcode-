#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    # 返回'00'和'11'是否都不在n的二进制表示中即可
    def hasAlternatingBits(self, n: int) -> bool:
        return '00' not in bin(n) and '11' not in bin(n)
# @lc code=end

