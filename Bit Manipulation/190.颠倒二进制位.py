#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # ans初始化为0，后面用于存储最终结果
        ans = 0
        # 进行32次循环移位
        for _ in range(32):
            # 将ans左移一位，然后将ans最右边的位置为n的最后一位
            # ans = (ans << 1) + (n & 1)
            ans = (ans << 1) | (n & 1)
            # n右移一位
            n = n >> 1
        # 返回最终结果
        return ans
    
    # 方法二：调API
    def reverseBits(self, n: int) -> int:
        x = bin(n)[:1:-1]
        if len(x) < 32:
            x += '0'*(32-len(x))
        return int(x,2)
# @lc code=end

