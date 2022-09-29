#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    # 动态规划（具体优化思路见官方解答）
    # 优化后的算法思想：
    # 每有一个「峰」到「谷」的下降趋势，down值才会增加，
    # 每有一个「谷」到「峰」的上升趋势，up值才会增加。
    # 且过程中down与up的差的绝对值恒不大于1，即up ≤ down + 1
    # 且down ≤ up + 1，于是有max(up,down+1) = down+1
    # 且max(up+1,down)=up+1。这样我们可以省去不必要的比较大小的过程。
    #
    # 复杂度分析：
    # 时间复杂度：O(n)，其中n是序列的长度。我们只需要遍历该序列一次。
    # 空间复杂度：O(1)。我们只需要常数空间来存放若干变量。
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        up, down = 1, 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)   
# @lc code=end

