#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#

# @lc code=start
class Solution:
    # 本题为相遇问题，移动距离最小的方式是所有元素都移动到中位数。理由如下：
    # 设 m 为中位数。a 和 b 是 m 两边的两个元素，且 b > a。要使 a 和 b 相等，它们总共移动的次数为 b - a，这个值等于 (b - m) + (m - a)，也就是把这两个数移动到中位数的移动次数。
    # 设数组长度为 N，则可以找到 N/2 对 a 和 b 的组合，使它们都移动到 m 的位置。
    # 编码思路：
    # 先对数组排序，然后利用双指针求得两指针所对应元素的差，然后将所有的差值加起来就是最终答案。
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            ans += nums[right] - nums[left]
            left += 1
            right -= 1
        return ans
# @lc code=end

