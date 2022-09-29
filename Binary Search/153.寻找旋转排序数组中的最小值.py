#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    # 模板二中的查找模糊值
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
# @lc code=end

