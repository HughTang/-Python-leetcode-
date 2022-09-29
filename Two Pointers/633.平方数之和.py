#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))
        while low <= high:
            if pow(low,2) + pow(high,2) < c:
                low += 1
            elif pow(low,2) + pow(high,2) > c:
                high -= 1
            else:
                return True
        return False
# @lc code=end

