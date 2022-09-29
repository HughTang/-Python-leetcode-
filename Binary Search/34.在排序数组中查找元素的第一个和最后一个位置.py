#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.search_left(nums,target)
        r = self.search_right(nums,target)
        return [l,r]
    
    # 寻找红色区域的最左侧元素
    def search_left(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r -l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r if r < len(nums) and nums[r] == target else -1 

    # 寻找蓝色区域的最右侧元素
    def search_right(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r -l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l if l > -1 and nums[l] == target else -1
# @lc code=end

