#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))

    # 打家劫舍1中的函数，直接拿来用即可
    def helper(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            b, a = max(a + nums[i], b), b
        return b
# @lc code=end

