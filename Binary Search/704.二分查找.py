#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start

class Solution:
    # 方法一：传统方法
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
    
    # 方法二：万能式（蓝色区域最右侧的值）
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r-l) // 2
            # 将nums[mid]==target的情况置于蓝色区域的最右侧值
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        # 判断target是否查找成功
        return l if nums[l] == target else -1

    # 方法三：万能式（红色区域最左侧的值）
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r-l) // 2
            # 将nums[mid]==target的情况置于红色区域的最左侧值
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        # 判断r是否越界，以及target是否查找成功
        return r if r < len(nums) and nums[r] == target else -1
