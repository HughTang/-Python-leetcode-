#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        pa, pb = len(a) - 1, len(b) - 1
        carry = 0
        while pa >= 0 or pb >= 0 or carry != 0:
            x = int(a[pa]) if pa >= 0 else 0
            y = int(b[pb]) if pb >= 0 else 0
            num = x + y + carry
            carry = num // 2
            ans = str(num % 2) + ans
            pa -= 1
            pb -= 1
        return ans

# @lc code=end

