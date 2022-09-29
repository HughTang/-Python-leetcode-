#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    # 尾部的 0 由 2 * 5 得来，2 的数量明显多于 5 的数量，因此只要统计有多少个 5 即可。
    # 对于一个数 N，它所包含 5 的个数为：N/5 + N/5² + N/5³ + ...，其中 N/5 表示不大于 N 的数中 5 的倍数贡献一个 5，N/5² 表示不大于 N 的数中 5² 的倍数再贡献一个 5 ...。
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
# @lc code=end

