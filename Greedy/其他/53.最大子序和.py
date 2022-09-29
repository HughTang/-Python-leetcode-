#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # 下面的两种方法时间复杂度都为O(N)，空间复杂度都为O(1)
    #
    # 方法一：贪心算法
    # 若当前指针指向的元素小于0，则丢弃当前元素之前的序列，并将当前元素的值作为下一个元素的之前序列之和；
    # 否则，则将当前元素加到之前的序列和中。
    # 然后每个元素遍历都要取cur_sum和max_sum的最大值赋给max_sum。
    # 最后返回max_sum即可
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1,len(nums)):
            # 这里的cur_sum+nums[i]与nums[i]做max可以判断cur_sum是否小于0
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum
    
    # 方法二：动态规划
    # 若前一个元素大于0，则将其加到当前元素上
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# @lc code=end

