#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        return nums
    
    def quick_sort(self,nums,low,high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivot-1)
            self.quick_sort(nums, pivot+1, high)
    
    def partition(self, nums, low, high):
        pos = random.randint(low,high)
        nums[low], nums[pos] = nums[pos], nums[low]
        pivot = nums[low]
        while low < high:
            while low < high and pivot <= nums[high]:
                high -= 1
            nums[low] = nums[high]
            while low < high and pivot >= nums[low]:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low
# @lc code=end

