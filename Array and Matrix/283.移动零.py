#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = 0
        for v in nums:
            if v != 0:
                nums[ret] = v
                ret += 1
        nums[ret:] = [0] * (len(nums)-ret)
# @lc code=end

