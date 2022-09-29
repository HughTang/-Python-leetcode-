#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x,y: x ^ y, nums + list(range(len(nums)+1)))
        # return sum(range(len(nums)+1)) - sum(nums)
# @lc code=end

